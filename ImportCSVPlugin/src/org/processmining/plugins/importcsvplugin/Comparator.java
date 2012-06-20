package org.processmining.plugins.importcsvplugin;



import java.util.Date;

import org.deckfour.xes.model.XEvent;

public class Comparator implements Comparable<Comparator> {
	
	private final Date date;
	private final XEvent event;
	
	

	public Comparator(Date date, XEvent event) {
		this.date = date;
		this.event = event;
	}

		

	public Date getDate() {
		return date;
	}



	public XEvent getEvent() {
		return event;
	}



	@Override
	public int compareTo(Comparator arg) {
		
		return date.compareTo(arg.getDate());
	}	
	
}