import sqlite3


# Comenzile pentru crearea tablourilor in baza de date ###############################
######################################################################################

QUERY_CREATE_TABLE_CLIENTS = '''CREATE TABLE IF NOT EXISTS Clients
(id INTEGER PRIMARY KEY AUTOINCREMENT, 
	last_name TEXT NOT NULL,
	first_name TEXT NOT NULL,
	company_id INT DEFAULT 0, 
	phone TEXT,
	gsm TEXT,
	mail TEXT,
	address TEXT, 
	city TEXT
	)'''

QUERY_CREATE_TABLE_WORKERS = '''CREATE TABLE IF NOT EXISTS Workers
(id INTEGER PRIMARY KEY AUTOINCREMENT,
	last_name TEXT NOT  NULL,
	first_name TEXT NOT NULL,
	DOB DATE NOT NULL,
	phone TEXT,
	gsm TEXT,
	post TEXT NOT NULL,
	e_date DATE NOT NULL,
	pay TEXT NOT NULL,
	login TEXT NOT NULL, 
	password TEXT NOT NULL 
	)'''

QUERY_CREATE_TABLE_PROJECTS = '''CREATE TABLE IF NOT EXISTS Projects
(id INTEGER PRIMARY KEY AUTOINCREMENT,
	client_id INT NOT NULL,  
	ser TEXT,				
	name TEXT NOT NULL,	
	fault TEXT,		
	found TEXT NOT NULL,  
	p_date DATE NOT NULL,  
	due DATE NOT NULL, 
	return DATE,  
	worker_id INT NOT NULL, 
	service_id INT NOT NULL, 
	change_piece TEXT, 
	price_piece TEXT, 
	warrant INT,  
	comments TEXT, 
	total_price TEXT 
	)'''

QUERY_CREATE_TABLE_PRODUCTS = '''CREATE TABLE IF NOT EXISTS Products
(id INTEGER PRIMARY KEY AUTOINCREMENT,
	ser TEXT NOT NULL,
	name TEXT NOT NULL,
	price TEXT NOT NULL,
	warrant INT NOT NULL DEFAULT 0,
	description TEXT, 
	stock INT NOT NULL DEFAULT 0
	)'''

QUERY_CREATE_TABLE_SALES = '''CREATE TABLE IF NOT EXISTS Sales
(id INTEGER PRIMARY KEY AUTOINCREMENT,
	worker_id INT NOT NULL,
	product_id INT, 
	client_id INT, 
	s_date DATE NOT NULL, 
	comments TEXT
	)'''

QUERY_CREATE_TABLE_SERVICES = '''CREATE TABLE IF NOT EXISTS Services
(id INTEGER PRIMARY KEY AUTOINCREMENT,
	type TEXT NOT NULL,
	price TEXT NOT NULL
	)'''

QUERY_CREATE_TABLE_COMPANIES = '''CREATE TABLE IF NOT EXISTS Companies
(id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	address TEXT,
	phone TEXT, 
	cod_fiscal TEXT,
	cod_decont TEXT,
	cod_bank TEXT,
	cod_trez TEXT)'''

######################################################################################

# Comenzile generice pentru extragerea datelor din baza de date ######################
######################################################################################

QUERY_GET_CLIENTS  = '''SELECT A.id as id, last_name, first_name, name as company_name 
						FROM Clients A, Companies B
						WHERE A.company_id = B.id
						UNION SELECT id, last_name, first_name, '' 
						FROM Clients WHERE company_id = ''
						ORDER BY A.id'''

QUERY_GET_WORKERS  = '''SELECT * FROM Workers'''

QUERY_GET_PROJECTS  = '''SELECT P.id, last_name as worker, ser, name as pr_name, p_date, due, return 
						FROM Projects P, Workers W 
						WHERE P.worker_id = W.id
						ORDER BY P.id'''

QUERY_GET_PRODUCTS = '''SELECT id, ser, name as dname, price, stock FROM Products
						ORDER BY id'''

QUERY_GET_SALES    = '''SELECT S.id, last_name as saler, ser, name as dname, s_date, price 
						FROM Sales S, Workers W, Products P
						WHERE S.worker_id =  W.id AND S.product_id = P.id
						ORDER BY S.id'''

QUERY_GET_SERVICES = '''SELECT * FROM Services ORDER BY id'''

QUERY_GET_COMPANIES = '''SELECT id, name as dname, address, phone FROM Companies
						 ORDER BY id'''

QUERY_GET_PRODUCTS_SHORT = '''SELECT ser, name FROM Products
							  WHERE stock > 0 
							  ORDER BY ser'''




#
# 
#  Clasa de baza ce lucreaza cu baza de date
#  Toata sintaxa SQL si toate operatiile asupra bazei de date se efectueaza
#  nemijlocit aici
class Database:

	def __init__(self, connection):
		self.connection = sqlite3.connect(connection)

		self.cursor = self.connection.cursor()

		self.cursor.execute(QUERY_CREATE_TABLE_CLIENTS)
		self.cursor.execute(QUERY_CREATE_TABLE_WORKERS)
		self.cursor.execute(QUERY_CREATE_TABLE_PRODUCTS)
		self.cursor.execute(QUERY_CREATE_TABLE_PROJECTS)
		self.cursor.execute(QUERY_CREATE_TABLE_SALES)
		self.cursor.execute(QUERY_CREATE_TABLE_SERVICES)	
		self.cursor.execute(QUERY_CREATE_TABLE_COMPANIES)	

		self.connection.commit()
		self.cursor.close()

	def InsertClient(self, client):
		self.cursor = self.connection.cursor()
		client.insert(0, None)
		self.cursor.execute('''INSERT INTO Clients VALUES 
			(?, ?, ?, ?, ?, ?, ?, ?, ?)''', client)
		rowid = self.cursor.lastrowid
		self.cursor.close()
		self.connection.commit()
		return rowid
	
	def InsertProject(self, project):
		self.cursor = self.connection.cursor()
		project.insert(0, None)
		self.cursor.execute('''INSERT INTO Projects VALUES 
			(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', project)

		rowid = self.cursor.lastrowid
		self.cursor.close()
		self.connection.commit()
		return rowid

	def InsertSale(self, sale):
		self.cursor = self.connection.cursor()
		sale.insert(0, None)
		self.cursor.execute('''INSERT INTO Sales VALUES 
			(?, ?, ?, ?, ?, ?)''', sale)
		rowid = self.cursor.lastrowid
		self.cursor.close()
		self.connection.commit()
		return rowid

	def InsertProduct(self, product):
		self.cursor = self.connection.cursor()
		product.insert(0, None)
		self.cursor.execute('''INSERT INTO Products VALUES 
			(?, ?, ?, ?, ?, ?, ?)''', product)
		rowid = self.cursor.lastrowid
		self.cursor.close()
		self.connection.commit()
		return rowid

	def InsertCompany(self, company):
		self.cursor = self.connection.cursor()
		company.insert(0, None)
		self.cursor.execute('''INSERT INTO Companies VALUES 
			(?, ?, ?, ?, ?, ?, ?, ?)''', company)
		rowid = self.cursor.lastrowid
		self.cursor.close()
		self.connection.commit()
		return rowid

	def InsertService(self, service):
		self.cursor = self.connection.cursor()
		service.insert(0, None)
		self.cursor.execute('''INSERT INTO Services VALUES 
			(?, ?, ?)''', service)
		rowid = self.cursor.lastrowid
		self.cursor.close()
		self.connection.commit()
		return rowid


	def DeleteItem(self, item_id, table):
		self.cursor = self.connection.cursor()
		self.cursor.execute('''DELETE FROM %s WHERE id = %s''' % (table, item_id))
		self.cursor.close()
		self.connection.commit()

	def GetClients(self):
		return self.GetTable(QUERY_GET_CLIENTS)

	def GetWorkers(self):
		return self.GetTable(QUERY_GET_WORKERS)

	def GetProjects(self):
		return self.GetTable(QUERY_GET_PROJECTS)

	def GetServices(self):
		return self.GetTable(QUERY_GET_SERVICES)

	def GetProducts(self):
		return self.GetTable(QUERY_GET_PRODUCTS)

	def GetCompanies(self):
		return self.GetTable(QUERY_GET_COMPANIES)

	def GetProductsShort(self):
		return self.GetTable(QUERY_GET_PRODUCTS_SHORT)

	def GetClient(self, client_id):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT * FROM Clients WHERE id = :id''', {"id" :client_id})
		data = self.cursor.fetchone()
		self.cursor.close()
		return data	

	def GetProject(self, project_id):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT * FROM Projects WHERE id = :id''', {"id" :project_id})
		data = self.cursor.fetchone()
		self.cursor.close()
		return data	

	def GetProduct(self, product_id):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT * FROM Products WHERE id = :id''', {"id" :product_id})
		data = self.cursor.fetchone()
		self.cursor.close()
		return data	


	def GetSale(self, sale_id):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT * FROM Sales WHERE id = :id''', {"id" :sale_id})
		data = self.cursor.fetchone()
		self.cursor.close()
		return data	


	def GetCompany(self, company_id):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT * FROM Companies WHERE id = :id''', {"id" :company_id})
		data = self.cursor.fetchone()
		self.cursor.close()
		return data	

	def GetService(self, service_id):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT * FROM Services WHERE id = :id''', {"id" :service_id})
		data = self.cursor.fetchone()
		self.cursor.close()
		return data	

	def GetWorker(self, worker_id):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT * FROM Workers WHERE id = :id''', {"id" :worker_id})
		data = self.cursor.fetchone()
		self.cursor.close()
		return data	

	def GetProductID(self, serial):
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute('''SELECT id FROM Products WHERE ser = :s''', {"s" :serial})
		data = self.cursor.fetchone()
		
		self.cursor.close()
		return data[0]

	def GetCompany_name_addr(self, company_id):
		self.cursor = self.connection.cursor()
		self.connection.row_factory = sqlite3.Row
		self.cursor.execute('''SELECT name, address FROM Companies WHERE id = %s''' %(company_id))
		data = self.cursor.fetchone()
		
		self.cursor.close()
		self.connection.commit()

		return data[0] + ' - ' + data[1]


	def GetProjectLarge(self, project_id):
				
		rdata = []
		data = self.GetProject(project_id)
		rdata.append(data)
		client_id  = data[1]
		service_id = data[10]
		worker_id  = data[9]
		data = self.GetClient(client_id)
		company_id  = data[3]
		rdata.append(data)
		data = self.GetService(service_id)
		rdata.append(data)
		data = self.GetWorker(worker_id)
		rdata.append(data)
		data = self.GetCompany(company_id)
		rdata.append(data)

		# ordinea: proiect, client, service, worker, company
		return rdata	

	def GetSaleLarge(self, sale_id):
		rdata = []
		data = self.GetSale(sale_id)
		rdata.append(data)
		product_id = data[2]
		data = self.GetProduct(product_id)
		rdata.append(data)
		return rdata


	def GetSales(self):
		return self.GetTable(QUERY_GET_SALES)


	def GetTable(self, query):
		
		self.cursor.close()
		self.connection.row_factory = sqlite3.Row
		self.cursor = self.connection.cursor()
		
		self.cursor.execute(query)
		
		data = self.get_cursor_data()
		
		self.cursor.close()
		return data

	def UpdateClient(self, client_id, client):
		
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Clients 
			SET
			last_name  = :lname,
			first_name = :fname,
			company_id = :c_id, 
			phone      = :phone, 
			gsm 	   = :gsm,
			mail       = :mail,
			address    = :addr, 
			city       = :city
			WHERE id = :id''',
			{"lname" : client[0],
			"fname"  : client[1],
			"c_id"   : client[2],
			"phone"  : client[3],
			"gsm"    : client[4],
			"mail"   : client[5],
			"addr"   : client[6],
			"city"   : client[7],
			"id"     : client_id})

		self.cursor.close()
		self.connection.commit()

	def UpdateProject(self, project_id, project):
		
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Projects 
			SET
			client_id    = :cl_id, 
			ser          = :ser,
			name         = :pr_name,
			fault        = :fault, 
			p_date       = :p_date,
			due          = :due, 
			worker_id    = :w_id
			WHERE id = :id''',
			{"cl_id"   : project[0],
			"ser"      : project[1],
			"pr_name"  : project[2],
			"fault"    : project[3],
			"p_date"   : project[5],
			"due"      : project[6],
			"w_id"     : project[8],
			"id"       : project_id})

		self.cursor.close()
		self.connection.commit()

	def FinishProject(self, project_id, project):
		
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Projects 
			SET
			found        = :found, 
			return       = :return, 
			service_id   = :s_id,
			change_piece = :ch_piece,
			price_piece  = :pr_piece,
			warrant      = :warr,
			comments     = :comm,
			total_price  = :t_price
			WHERE id = :id''',
			{"found"   : project[0],
			"return"   : project[1],
			"s_id"     : project[2],
			"ch_piece" : project[3],
			"pr_piece" : project[4],
			"warr"     : project[5],
			"comm"     : project[6],
			"t_price"  : project[7],
			"id"       : project_id})

		self.cursor.close()
		self.connection.commit()

	def UpdateService(self, service_id, service):
		
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Services 
			SET
			type  = :type,
			price = :price
			WHERE id = :id''',
			{"type"  : service[0],
			"price"  : service[1],
			"id"     : service_id})

		self.cursor.close()
		self.connection.commit()


	def UpdateProduct(self, product_id, product):
		
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Products 
			SET
			ser         = :ser,
			name        = :name,
			price       = :price,
			warrant     = :warrant,
			description = :descr,
			stock       = :stock
			WHERE id = :id''',
			{"ser"    : product[0],
			"name"    : product[1],
			"price"   : product[2],
			"warrant" : product[3],
			"descr"   : product[4],
			"stock"   : product[5],
			"id"     : product_id})

		self.cursor.close()
		self.connection.commit()


	def UpdateCompany(self, company_id, company):
		
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Companies 
			SET
			name       = :name,
			address    = :addr,
			phone      = :phone,
			cod_fiscal = :cf,
			cod_decont = :cd,
			cod_bank   = :cb,
			cod_trez   = :ct
			WHERE id = :id''',
			{"name"   : company[0],
			"addr"    : company[1],
			"phone"   : company[2],
			"cf"      : company[3],
			"cd"      : company[4],
			"cb"      : company[5],
			"ct"      : company[6],
			"id"      : company_id})

		self.cursor.close()
		self.connection.commit()

	def UpdateSale(self, sale_id, sale):
		
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Sales
			SET
			worker_id  = :w_id,
			client_id  = :c_id,
			s_date     = :s_d,
			comments   = :com
			WHERE id   = :id''',
			{"w_id"    : sale[0],
			"c_id"     : sale[2],
			"s_d"      : sale[3],
			"com"      : sale[4],
			"id"       : sale_id})

		self.cursor.close()
		self.connection.commit()

	def RemoveFromStock(self, product_id):
		self.cursor = self.connection.cursor()
		self.cursor.execute('''UPDATE Products
			SET
			stock = stock - 1
			WHERE id = :id''',
			{"id"      : product_id})

		self.cursor.close()
		self.connection.commit()

	def get_cursor_data(self):

		data = []
		columns = []
		for col in self.cursor.description:
			columns.append(col[0])

		items = self.cursor.fetchall()
		data.append(items)
		data.append(columns)

		return data


	def CheckLogin(self, login, password):

		self.cursor.close()
		self.cursor = self.connection.cursor()
		self.cursor.execute('''SELECT * FROM Workers WHERE login = :log
			AND password = :pass''', {"log" : login, "pass" : password})
		data = self.cursor.fetchone() 
		if data == None:
			return None
		else:
			logger = []
			logger.append(data[0])
			logger.append(data[1] + ' ' + data[2])
			return logger
