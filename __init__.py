from flask import Flask,render_template,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
sources_gms =[{
    'source':'World History: The Modern Era',
    'link':'http://databases.abc-clio.com',
    'username':'grover',
    'password':'middle'
},
{
    'source':'Classroom Video on Demand',
    'link':'http://www.fofweb.com/subscription',
    'username':'wwptgms',
    'password':'wwptgms'
},
{
    'source':'BrainPOP',
    'link':'http://www.brainpop.com',
    'username':'wwptgms',
    'password':'wwptgms'
},
{
    'source':'CQ Researcher Online',
    'link':'http://library.cqpress.com/cqresearcher',
    'username':'thomas',
    'password':'grover'
},
{
    'source':'Discovery Education Science',
    'link':'http://discoveryeducation.com',
    'username':'thomas',
    'password':'grover'
},
{
    'source':'Explora',
    'link':'http://search.ebscohost.com',
    'username':'thomasgrover',
    'password':'middle'
},
{
    'source':'Encyclopaedia Britannica Online School Edition',
    'link':'http://www.school.eb.com',
    'username':'grover',
    'password':'middle'
},
{
    'source':'Global Issues in Context',
    'link':'http://infotrac.galegroup.com/itweb/prin25719',
    'username' : 'grover',
    'password':'none'
},
{
    'source':'netTrekker',
    'link':'http://www.nettrekker.com',
    'username':'wwpgms',
    'password':'wwp01'
},
{
    'source':'The New York Times Electronic Edition',
    'link':'http://eedition.nytimes.com',
    'username':'900222001',
    'password':'900222001'
},
{
    'source':'NoodleBib',
    'link':'http://my.noodletools.com',
    'username':'thomas',
    'password':'grover'
},
{
    'source':'ProQuest Historical Newspapers – Graphical',
    'link':'http://hn.bigchalk.com',
    'username':'thomas',
    'password':'grover'
},{
    'source':'SIRS Issues Researcher',
    'link':'http://ars.sirs.com',
    'username':'thomas',
    'password':'grover'
}]
sources_hs = [
    {
        'source':'ABC-CLIO',
        'link':'http://www.socialstudies.abc-clio.com',
        'username':'wwphss',
        'password':'wwphss'
    },
    {
        'source':'CQ Researcher',
        'link':'https://library.cqpress.com/cqresearcher',
        'username':'westwindsor',
        'password':'plainsboro'
    },
    {
        'source':'EBSCOhost',
        'link':'http://search.epnet.com/login.asp',
        'username':'cjrlc117',
        'password':'SouthPirates3!'
    },
    {
        'source':'Facts on File',
        'link':'http://www.fofweb.com/subscription',
        'username':'wwphss',
        'password':'pirate'
    },
    {
        'source':'Gale Student Resources in Context',
        'link':'http://infotrac.galegroup.com/itweb/prin24068',
        'username':'none',
        'password':'wwphss'
    },
    {
        'source':'Gale Virtual Reference Library',
        'link':'http://infotrac.galegroup.com/itweb/prin24068',
        'username':'none',
        'password':'wwphss'
    },
    {
        'source':'JSTOR',
        'link':'www.jstor.org',
        'username':'wwpsouth',
        'password':'pirates'
    },
    {
        'source':'JSTOR Global Plants',
        'link':'plants.jstor.org',
        'username':'wwpsouth',
        'password':'pirates'
    },
    {
        'source':'netTrekker',
        'link':'http://www.nettrekker.com',
        'username':'wwphss',
        'password':'wwp01'
    },
    {
        'source':'The New York Times',
        'link':'http://www.nytimes.com',
        'username':'none',
        'password':'none'
    },
    {
        'source':'NoodleTools',
        'link':'http://www.noodletools.com',
        'username':'WWPHSS',
        'password':'Pirate'
    },
    {
        'source':'Proquest Historical Newspapers',
        'link':'http:www.proquestk12.com/my products',
        'username':'wwphss',
        'password':'pirate'
    },
    {
        'source':'Proquest CultureGrams',
        'link':'http://www.proquestk12.com/my products',
        'username':'wwphss',
        'password':'pirate'
    }]
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'