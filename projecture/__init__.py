__version__ = '0.1.3'

from .projecture import ProjectsCollection

__projects = ProjectsCollection()

list_projects = __projects.list_projects
create_project = __projects.create_project
