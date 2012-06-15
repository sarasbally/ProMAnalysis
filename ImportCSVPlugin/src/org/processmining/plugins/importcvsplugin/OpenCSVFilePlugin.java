package org.processmining.plugins.importcvsplugin;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

import org.deckfour.xes.extension.std.XConceptExtension;
import org.deckfour.xes.extension.std.XOrganizationalExtension;
import org.deckfour.xes.factory.XFactory;
import org.deckfour.xes.factory.XFactoryRegistry;
import org.deckfour.xes.model.XAttributeMap;
import org.deckfour.xes.model.XEvent;
import org.deckfour.xes.model.XLog;
import org.deckfour.xes.model.XTrace;
import org.deckfour.xes.model.impl.XAttributeLiteralImpl;
import org.deckfour.xes.model.impl.XAttributeMapImpl;
import org.deckfour.xes.model.impl.XAttributeTimestampImpl;
import org.deckfour.xes.model.impl.XEventImpl;
import org.processmining.contexts.uitopia.annotations.UIImportPlugin;
import org.processmining.framework.abstractplugins.AbstractImportPlugin;
import org.processmining.framework.plugin.PluginContext;
import org.processmining.framework.plugin.annotations.Plugin;

import au.com.bytecode.opencsv.CSVReader;


@Plugin(name = "Import CVS", parameterLabels = { "Import" }, returnLabels = { "Imported" }, returnTypes = { XLog.class })
@UIImportPlugin(description = "Import CVS", extensions = { "cvs" })

public class OpenCSVFilePlugin extends AbstractImportPlugin{

	private XFactory factory;
	private XOrganizationalExtension organizationalExtension;
	private XLog log;
	private XConceptExtension conceptExtension;

	@Override
	protected Object importFromStream(PluginContext context, InputStream input,
			String filename, long fileSizeInBytes) throws Exception {

		CSVReader reader = new CSVReader(new InputStreamReader(input), ';');
		
		initializeLog();
		Map<String,XTrace> maptrace = new HashMap<String,XTrace>();
		System.out.println(input.toString());
		int numline=0;
		 String [] nextLine;
		    while ((nextLine = reader.readNext()) != null) {
		    	if(numline>0){
		        // nextLine[] is an array of values from the line
		    	String time=nextLine[2];
		    	
		    	
		    	//if(time==null)time="15/02/2012  15:04:00";
		    	if(!maptrace.containsKey(nextLine[0])){
					XTrace trace = this.createAndAddTrace(String.valueOf(nextLine[0]));
					trace.add(makeEvent(nextLine[4], time,nextLine[5]));
					maptrace.put(nextLine[0], trace);
				}else{
					XTrace trace = maptrace.get(nextLine[0]);
					trace.add(makeEvent(nextLine[4],time,nextLine[5]));
					maptrace.put(nextLine[0], trace);
				}
		    	}
		    	numline++;
		    
		    }
		
		/*String strLine = "";
		StringTokenizer st = null;
		int lineNumber = 0, tokenNumber = 0;
		while( (strLine = br.readLine()) != null)
		{

			if(lineNumber>0){
				//break comma separated line using ","
				st = new StringTokenizer(strLine, ";");

				// XTrace trace = this.createAndAddTrace(String.valueOf(lineNumber));
				String name="a";
				String timestamp = "";
				String rfc = "",res="";
				while(st.hasMoreTokens())
				{

					switch (tokenNumber) {
					case 4: name = st.nextToken() ; break;
					case 2: timestamp = st.nextToken() ; break;
					case 0: rfc = st.nextToken() ; break;
					case 5: res = st.nextToken() ; break;
					default: st.nextToken() ; break;

					}
					//display csv values
					
					tokenNumber++;
				} 
				




				//reset token number
				tokenNumber = 0;
			}
			lineNumber++;
		}*/
		return log;
	} 

	private XEvent makeEvent(String name, String timestamp, String  res)  {
		SimpleDateFormat formatter = new SimpleDateFormat("dd-MM-yyyy HH:mm");
		Date time;
		try {
			time = (Date)formatter.parse(timestamp);

			XAttributeMap attMap = new XAttributeMapImpl();
				putLiteral(attMap, "concept:name", name);
			putLiteral(attMap, "lifecycle:transition", "complete");
			if(res.trim().length()!=0){
				if(res!=null){
				putLiteral(attMap, "org:resource", res);
				}
			}
			
			putTimestamp(attMap, "time:timestamp", time);
			
			XEvent newEvent = new XEventImpl(attMap);
			return newEvent;
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
	}

	private void putLiteral(XAttributeMap attMap, String key, String value) {
		attMap.put(key, new XAttributeLiteralImpl(key, value));
	}

	private void putTimestamp(XAttributeMap attMap, String key, Date value) {
		attMap.put(key, new XAttributeTimestampImpl(key, value));
	}

	private void initializeLog() {
		factory = XFactoryRegistry.instance().currentDefault();
		conceptExtension = XConceptExtension.instance();
		organizationalExtension = XOrganizationalExtension.instance();
		log = factory.createLog();
		log.getExtensions().add(conceptExtension);
		log.getExtensions().add(organizationalExtension);




	}

	public XTrace createAndAddTrace(String name) {
		XTrace trace = factory.createTrace();
		log.add(trace);
		trace.getAttributes().put(XConceptExtension.KEY_NAME,
				factory.createAttributeLiteral(XConceptExtension.KEY_NAME, name, conceptExtension));

		return trace;
	}
}
