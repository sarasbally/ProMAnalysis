package org.processmining.plugins.importcsvplugin;

import java.util.Date;

import org.deckfour.xes.extension.std.XTimeExtension;
import org.deckfour.xes.model.XAttribute;
import org.deckfour.xes.model.XAttributeMap;
import org.deckfour.xes.model.XAttributeTimestamp;
import org.deckfour.xes.model.impl.XEventImpl;

public class CollEvent extends XEventImpl implements Comparable<CollEvent>  {

	public CollEvent(XAttributeMap attMap) {
		// TODO Auto-generated constructor stub
		super(attMap);
	}

	@Override
	public int compareTo(CollEvent o) {
		 Date date = ((XAttributeTimestamp) this.getAttributes().get(XTimeExtension.KEY_TIMESTAMP)).getValue();
		 Date date1 = ((XAttributeTimestamp) o.getAttributes().get(XTimeExtension.KEY_TIMESTAMP)).getValue();
		return date.compareTo(date1);
	}

}
