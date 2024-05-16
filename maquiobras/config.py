SQLALCHEMY_DATABASE_URI = 'sqlite:////local.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False


SQLALCHEMY_BINDS = {
    #'paradigmasolucionesit': 'mysql+pymysql://',
    'maquiobrasdb': 'mysql+pymysql://root:@localhost:3306/maquiobrasdb',
}
