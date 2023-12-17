import os
import sys

Services_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Services'))
sys.path.append(Services_path)



workflow_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app','interactions'))
sys.path.append(workflow_path)

#engine itself
engine_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Engine'))
sys.path.append(engine_path)

interface_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Interface'))
sys.path.append(interface_path)


#adding user defined ones..
components = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app','Entities','components'))
agents_resources = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','app','Entities'))
Schema_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app','Schema'))
sys.path.append(Schema_path)
sys.path.append(components)
sys.path.append(agents_resources)