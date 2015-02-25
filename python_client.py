from py4j.java_gateway import JavaGateway, Py4JError

SIMPLE_PYTHON_SCRIPT_1 = "a = 2"

SIMPLE_PYTHON_SCRIPT_2 = """l = gateway.jvm.java.util.ArrayList()
l.append("a")
l.append("b")
"""

class PythonInterpreter(object):
    
    def __init__(self, gateway):
        self.gateway = gateway
    
    def callPython(self, pythonCode):
        locals = {}
        globals = {"gateway": self.gateway}
        exec(pythonCode, globals, locals)
        
        # Return the first local defined in python code we found...
        locals_list = list(locals.values())
        returnValue = None
        if locals_list:
            returnValue = locals_list[0]
        return returnValue
    
    class Java:
        implements = ["com.infobart.arbitrarypython.PythonInterpreter"]

def main():
    gateway = JavaGateway(start_callback_server=True)
    interpreter = PythonInterpreter(gateway)
    gateway.entry_point.setPythonInterpreter(interpreter)
    
    gateway.entry_point.interpret(SIMPLE_PYTHON_SCRIPT_1)
    gateway.entry_point.interpret(SIMPLE_PYTHON_SCRIPT_2)
    
    # Will raise an exception because the Java side is closing the connection.
    # Something to polish a bit...
    try:
        gateway.entry_point.runFromJava()
    except Py4JError:
        pass
    

if __name__ == "__main__":
    main()