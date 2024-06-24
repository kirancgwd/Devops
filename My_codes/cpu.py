import os                                                                                                                                                       
du = os.popen("df -h").readlines()
from pprint import pprint
pprint(du)

