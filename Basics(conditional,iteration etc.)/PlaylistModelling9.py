playlist={
	'title':'Sample',
	'Author':'Khalifa',				
	'songs':[				#THIS IS NESTED DATA STRUCTURE OF DICTIONARY AND LIST
		{'title':'song1','artist':['name1'],'duration':3.5},
		{'title':'song2','artist':['name2','name3'],'duration':4.25},
		{'title':'song3','artist':['name4'],'duration':3.0}
	]
}
print(playlist)
print("\n \n")
total_duration=0
for song in playlist['songs']:
	total_duration+=song['duration']

print(f"The total duration of the playlist is : {total_duration}")