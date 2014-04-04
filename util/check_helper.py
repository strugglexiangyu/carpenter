# -*- coding:utf8 -*-

def split_ip(ip):
	add_ip = ''
	ip_split=ip.split('\n')
	for x in range(len(ip_split)):
		add_ip += ip_split[x]+'|'
	return add_ip

def ip_check(ip):
	q = ip.split('.')
	return len(q) == 4 and len(filter(lambda x: x >= 0 and x <= 255, map(int, filter(lambda x: x.isdigit(), q)))) == 4