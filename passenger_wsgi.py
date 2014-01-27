import sys, os

DEBUG = False

cwd = os.getcwd()
site_name = 'PandaPoker' # THE NAME OF YOUR PROJECT
site_home = os.path.join(cwd,site_name)
pinax_env_bin = os.path.join(cwd,'pinax-env/bin') # THE RELATIVE PATH TO YOUR VIRTUALENV BIN DIRECTORY

#Check that the version of python is 2.6 or greater
#if sys.hexversion < 0x2060000:
#   os.execl("/home/user/bin/python2.6", "python2.6", *sys.argv)

# Invoke the virtualenv
INTERP = '%s' % (os.path.join(pinax_env_bin,'python'))
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.stdout = sys.stderr
sys.path.append(site_home)
sys.path.append(os.path.join(site_home,'apps'))
sys.path.append(os.path.join(cwd,'pinax-env/lib/python2.6/site-packages/pinax'))
sys.path.append(os.path.join(cwd,'pinax-env/lib/python2.6/site-packages/pinax/apps'))
sys.path.append(os.getcwd()) 
os.environ['DJANGO_SETTINGS_MODULE'] = '.'.join([site_name,"settings"])
import django.core.handlers.wsgi
from paste.exceptions.errormiddleware import ErrorMiddleware
application = django.core.handlers.wsgi.WSGIHandler()

#Define a test application to check that the ErrorMiddleware is working 
def testapplication(environ, start_response):
   status = '200 OK'
   output = 'Hello World! Running Python version %s\n\n' % (sys.version)
   response_headers = [('Content-type', 'text/plain'),
                       ('Content-Length', str(len(output)))]
   
   #Check that the ErrorMiddleware works by uncommenting the next line
   #raise("error")
   start_response(status, response_headers)
   return [output] 

application = ErrorMiddleware(application, debug=DEBUG)
