def time():
	#grabs your latitude, longitude and Time zone
	import requests, json, datetime
	current_year = datetime.datetime.now().strftime('%Y')
	loc_request=requests.get('http://ip-api.com/json')
	type(loc_request)
	loc_request.status_code==requests.codes.ok
	loc_request_json_data = loc_request.text
	Location_info = json.loads(loc_request_json_data)



	# your location data
	longi = str(Location_info['lon'])
	latit = str(Location_info['lat'])
	city = Location_info['city']
	region = Location_info['timezone']



	#using your location data to get customized shabbos data
	#link is for master heb cal calendar api
	heb_cal_address='http://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year='+current_year+'&month=x&ss=on&mf=on&c=on&geo=pos&latitude=['+latit+']&longitude=['+longi+']&tzid=['+region+']&m=50&s=off'

	#begin main loop
	count = 0
	while count<1:
		count +=1

		import json, requests, datetime, time
		from subprocess import call

	    	res = requests.get(heb_cal_address)
		ready = json.loads(res.text)

		#beginning of main while loop that should hold until candles followed by havdala
	    	#parsing json for times
	    	data = ready.get('items')

		for i in range(0, len(data)):
			if data[i].get('category') == 'candles' or data[i].get('category') == 'havdalah':
		       		date_retrival= data[i].get('date')
	        		date_retrival2 = date_retrival.split('T')
				time = date_retrival2[1].split('-')
				date_plus_time = date_retrival2[0] +" "+ time[0]

	        #date_obj is next candlelighting/havdalah time and date

				date_obj = datetime.datetime.strptime(date_plus_time, '%Y-%m-%d %H:%M:%S')
				if date_obj >= datetime.datetime.now() and date_obj - datetime.datetime.now() < datetime.timedelta(hours = 70):
					upcoming_event =date_obj
	                		event_date = upcoming_event.strftime('%A %B %d %Y')
	                		event_time = upcoming_event.strftime('%I %M %p')
					if data[i].get('category') == "candles":
						event_type = "Candlelighting"
					elif data[i].get('category') == "havdalah":
						event_type = "Havdalah"
					else:
						event_type = "unclear event"
					return( event_type + " on "+ event_date + " will be at " + event_time)

print(time())	
