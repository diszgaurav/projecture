"""project bootstrap for various frameworks and languages
"""
__author__ = "Gaurav Verma"
__email__  = "diszgaurav@gmail.com"

#----------------------------------------------------------------------
import os
import logging
import shutil
import re
import fileinput
import time

#----------------------------------------------------------------------
class ProjectsCollection(object):
    """Projects Collection Class
    """

    def __init__(self):

        self.__projecture_dir = os.path.abspath(os.path.dirname(__file__))
        self.__projects_dir = os.path.join(self.__projecture_dir, 'projects')

        # build supported languages
        self.__supported_projects = []
        for prj in os.listdir(self.__projects_dir):
            # TODO: add dis-qualifiers
            self.__supported_projects.append(prj)


    def create_project(self, project,
                       project_type='python',
                       author_name='author_name',
                       author_email='author_email',
                       about='short description of project',
                       force=False):
        """create bootstrap project structure for specified language

        :returns: execution status
        :rtype: int

        """

        if project_type not in self.__supported_projects:
            msg = 'project for "{}" not supported!'.format(project_type)
            logging.error(msg)
            print msg
            return 1

        project_dst, project_name = self.__get_project_path_name(project)

        project_src = os.path.join(self.__projects_dir, project_type)
        project_src = os.path.join(project_src, 'myproject')

        if os.path.exists(project_dst):
            if not force:
                msg = 'Project "{}" already exists. Use -f or --force to overwrite it'.format(project)
                logging.info(msg)
                print msg
                return 0
            else:
                shutil.rmtree(project_dst)

        shutil.copytree(project_src, project_dst, symlinks=True)

        logging.debug('renaming dirs/files')
        # need to walk twice!
        for i in range(2):
            for root, dirs, files in os.walk(project_dst):
                for f in dirs if i else files:
                    f_old = os.path.join(root, f)
                    # file content
                    if not i:
                        for line in fileinput.input(files=f_old, inplace=True):
                            line = re.sub('myproject:author_name', author_name.title(), line)
                            line = re.sub('myproject:author_email', author_email, line)
                            line = re.sub('myproject:year', time.strftime('%Y'), line)
                            line = re.sub('myproject:about', about, line)
                            line = re.sub('myproject', project_name, line)
                            print line.rstrip()
                    # file names
                    f_new = os.path.join(root, re.sub('myproject', project_name, f))
                    os.rename(f_old, f_new)

        exit_msg = '"{}" project created for {}'.format(project_name, project_type)
        logging.info(exit_msg)
        print exit_msg

        return 0


    def list_projects(self):
        """returns all supported projects as a list

        :returns: supported projects
        :rtype: list

        """

        return self.__supported_projects


    def __get_project_path_name(self, project):
        """retrieve project's absolute path and just name

        :param project: project name with absolute/relative path
        :returns: project path and name
        :rtype: tuple

        """

        project_name = os.path.split(project)[-1]
        project_path = os.path.abspath(project)
        return (project_path, project_name)
