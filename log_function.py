def log(x, base):
	log_b = 2
	while x != int(round(base ** log_b)):
		log_b += 0.01
	print(log_b)
	return int(round(log_b))

log(10,2)
