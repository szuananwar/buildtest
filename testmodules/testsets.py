from parser import *
from tools.generic import *
from tools.cmake import *

def run_testset(software,toolchain,testset,verbose):
	""" checks the testset parameter to determine which set of scripts to use to create tests """

	appname,appversion=get_software_name_version(software)

	source_app_dir=""
	codedir=""
	logcontent = ""
	runtest = False

	if appname in PYTHON_APPS and testset == "python":
	        source_app_dir=os.path.join(BUILDTEST_SOURCEDIR,"python")
                runtest=True
    
        if appname in PERL_APPS and testset == "perl":
        	source_app_dir=os.path.join(BUILDTEST_SOURCEDIR,"perl")
                runtest=True

        # condition to run R testset
        if appname in ["R"] and testset == "R":
        	source_app_dir=os.path.join(BUILDTEST_SOURCEDIR,"R")
                runtest=True

        if runtest == True:
        	codedir=os.path.join(source_app_dir,"code")
                logcontent+=testset_generator(software,toolchain,codedir,verbose)

	return logcontent
def testset_generator(software,toolchain,codedir,verbose):
	logcontent = "--------------------------------------\n"
	logcontent = "function: testset_generator \n"
	logcontent = "--------------------------------------\n"

	wrapper=""
        appname=software[0]
        appver=software[1]
        tcname=toolchain[0]
        tcver=toolchain[1]

	app_destdir = os.path.join(BUILDTEST_TESTDIR,"ebapp",appname,appver,tcname,tcver)
	cmakelist = os.path.join(app_destdir,"CMakeLists.txt")
	if os.path.isdir(codedir):
		for root,subdirs,files in os.walk(codedir):
			for file in files:
				# get file name without extension
				fname = os.path.splitext(file)[0]
				# get file extension
				ext = os.path.splitext(file)[1]
			
				if ext == ".py":
					wrapper = "python"
				elif ext == ".R":
					wrapper = "Rscript"
				elif ext == ".pl":
					wrapper = "perl"
				else:
					continue

				cmd = wrapper + " " + os.path.join(root,file)
				subdir = os.path.basename(root)
				subdirpath = os.path.join(app_destdir,subdir)
				if not os.path.exists(subdirpath):
					os.mkdir(subdirpath)
				testname = fname + ".sh"
				testpath = os.path.join(subdirpath,testname)
				fd = open(testpath,'w')
				header=load_modules(software,toolchain)
				fd.write(header)
				fd.write(cmd)
				fd.close()
			
				logcontent+="TestPath: " + testpath
				logcontent+="\n--------------------------------------------\n"
				logcontent+=open(testpath,'r').read()
				logcontent+="\n--------------------------------------------\n"
				
				cmakelist = os.path.join(subdirpath,"CMakeLists.txt")
				logcontent+=add_test_to_CMakeLists(appname,appver,tcname,tcver,app_destdir,subdir,cmakelist,testname)
				print "Creating Test: ", testpath
	return logcontent	