package org.processmining.plugins.importcvsplugin;

import java.io.InputStream;

import org.deckfour.xes.model.XLog;
import org.processmining.contexts.uitopia.annotations.UIImportPlugin;
import org.processmining.framework.abstractplugins.AbstractImportPlugin;
import org.processmining.framework.plugin.PluginContext;
import org.processmining.framework.plugin.annotations.Plugin;

@Plugin(name = "Import CVS", parameterLabels = { "Import" }, returnLabels = { "Imported" }, returnTypes = { XLog.class })
@UIImportPlugin(description = "Import CVS", extensions = { "cvs" })

public class OpenCVSFilePlugin extends AbstractImportPlugin{

	@Override
	protected Object importFromStream(PluginContext context, InputStream input,
			String filename, long fileSizeInBytes) throws Exception {
		XLog newLog = null;
		System.out.println(input.toString());
		
		return newLog;
	} 
}
