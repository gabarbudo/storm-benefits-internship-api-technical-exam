from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/companydb'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# company model
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    num_employees = db.Column(db.Integer)
    location = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    industry = db.Column(db.String(255))

    def __init__(self, name, num_employees, location, email, industry):
        self.name = name
        self.num_employees = num_employees
        self.location = location
        self.email = email
        self.industry = industry

# ensures that all endpoints have a JSON response
class CompanySchema(ma.Schema):
	class Meta:
		fields = ('name', 'num_employees', 'location', 'email', 'industry')

company_schema = CompanySchema()
companies_schema = CompanySchema(many=True)

# lists all company records
@app.route('/company/', methods = ['GET'])
def index():
	all_companies = Company.query.all()
	result = companies_schema.dump(all_companies)
	return jsonify(result.data)

# gets company record details by id
@app.route('/company/<int:id>/')
def get_company(id):
	company = Company.query.get(id)
	return company_schema.jsonify(company)

# inserts new company record
@app.route('/company/', methods = ['POST'])
def create_company():
    name = request.json['name']
    num_employees = request.json['num_employees']
    location = request.json['location']
    email = request.json['email']
    industry = request.json['industry']

    new_company = Company(name, num_employees, location, email, industry)
    result = company_schema.dump(new_company)

    db.session.add(new_company)
    db.session.commit()

    return jsonify(result.data), 201

# deletes company record
@app.route('/company/<int:id>/', methods = ['DELETE'])
def delete_company(id):
	company = Company.query.get(id)
	db.session.delete(company)
	db.session.commit()

	return jsonify({ 'result': True })

# updates existing company record
@app.route('/company/<int:id>/', methods = ['PUT'])
def update_company(id):
    company = Company.query.get(id)
    name = request.json['name']
    num_employees = request.json['num_employees']
    location = request.json['location']
    email = request.json['email']
    industry = request.json['industry']

    company.name = name
    company.num_employees = num_employees
    company.location = location
    company.email = email
    company.industry = industry
    
    db.session.commit()
    return company_schema.jsonify(company)

# filters list of companies by company name using wildcard search
@app.route('/company/<string:name>/')
def search_company(name):
	company = Company.name.like('%' + name + '%')
	filter_company = Company.query.filter(company).all()
	result = companies_schema.dump(filter_company)
	return jsonify(result.data)

if __name__ == '__main__':
	app.run()

