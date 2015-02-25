package com.infobart.arbitrarypython;

public class EntryPoint {

	private PythonInterpreter pythonInterpreter;

	public PythonInterpreter getPythonInterpreter() {
		return pythonInterpreter;
	}

	public void setPythonInterpreter(PythonInterpreter pythonInterpreter) {
		this.pythonInterpreter = pythonInterpreter;
	}
	
	public void interpret(String pythonCode) {
		Object returnValue = this.pythonInterpreter.callPython(pythonCode);
		System.out.println(returnValue);
	}
	
	public void runFromJava() {
		String pythonCode = "gateway.jvm.System.out.println(\"Hello World\")";
		this.pythonInterpreter.callPython(pythonCode);
		pythonCode = "gateway.shutdown()";
		this.pythonInterpreter.callPython(pythonCode);
	}
	
}
