
def main():
	import shelve
	#make our data persistent
	s = shelve.open('drows.db')
	try:
		#created first dict and made a dict of dicts
		s['foo'] = {1:'foo', 2:'bar', 3:'LumberJack', 4:'I work all day'}
		s['bar'] = {1:'foo', 2:'bar', 3:'LumberJack', 4:'I work all day'}
	finally:
		s.close()	

	s = shelve.open('drows.db')	
	
	for item in s:
		print("%s: %s" % (item, s[item]))


def delrow(s, rowkey):
	try:
		del s[rowkey]
	except:
		pass

if __name__ == "__main__":
	main()