import csv
import matplotlib.pyplot as plt

def readRowerData(infile):
	rowerData = []
	with open(infile, 'rU') as f:
		reader = csv.reader(f)
		for row in reader:
			name = row[0]
			fortymin = int(row[1])
			onemin = int(row[2])
			repmax = int(row[3])
			maxwatt = int(row[4])
			weight = int(row[5])

			entry = {'Name': name, 'Forty Minute': fortymin, 'One Minute': onemin, \
					'Rep Max': repmax, 'Max Watt': maxwatt, 'Weight': weight}
			rowerData.append(entry)
	return rowerData

def readTimeData(infile):
	timeData = []
	with open(infile, 'rU') as f:
		reader = csv.reader(f)
		for row in reader:
			# print row[0]
			if (row[0] != ''):
				velocity = float(row[0])
			rowers = []
			for i in range(4, 12):
				rowers.append(row[i])
			entry = {'Velocity': velocity, 'Rowers': rowers}
			timeData.append(entry)
	timeData.pop()
	return timeData

def plotData(rowerData, timeData):
	y_values = []
	for row in timeData:
		# print row['Velocity']
		y_values.append(row['Velocity'])
	x_product = []
	x_forty = []
	x_one = []
	x_repmax = []
	x_watt = []
	x_weight = []
	x_area = []
	for row in timeData:
		forty_sum = 0
		one_sum = 0
		repmax_sum = 0
		watt_sum = 0
		weight_sum = 0
		product = 0
		area = 0
		for rower in row['Rowers']:
			for entry in rowerData:
				if (rower == entry['Name']):
					a = (entry['Forty Minute'] / 11881.0)
					b = (entry['One Minute'] / 375.0)
					c = (entry['Rep Max'] / (2.0 * entry['Weight']))
					d = (entry['Max Watt'] / 1100.0)
					forty_sum += (entry['Forty Minute'] / 11881.0)
					one_sum += (entry['One Minute'] / 375.0)
					repmax_sum += (entry['Rep Max'] / (2.0 * entry['Weight']))
					watt_sum += (entry['Max Watt'] / 1100.0)
					weight_sum += entry['Weight']
					product += (entry['Forty Minute'] / 11881.0)  * (entry['One Minute'] / 375.0) * (entry['Rep Max'] / (2.0 * entry['Weight'])) * (entry['Max Watt'] / 1100.0)
					area += 0.5 * ( (a*b) + (b*c) + (c*d) + (a*d))
					break
		x_area.append(area / 8.0)
		x_product.append(product / 8.0)
		x_forty.append(forty_sum / 8.0)
		x_one.append(one_sum / 8.0)
		x_repmax.append(repmax_sum / 8.0)
		x_watt.append(watt_sum / 8.0)
		x_weight.append(weight_sum / 8.0)

	fig_area = plt.figure()
	axes_area = fig_area.add_subplot(1, 1, 1)
	axes_area.plot(x_area, y_values, 'o')
	axes_area.set_title('Velocit vs. Area of Average Values')

	fig_product = plt.figure()
	axes_product = fig_product.add_subplot(1, 1, 1)
	axes_product.plot(x_product, y_values, 'o')
	axes_product.set_title('Velocit vs. Product of Average Values')

	# fig_forty = plt.figure()
	# axes_forty = fig_forty.add_subplot(1, 1, 1)
	# axes_forty.plot(x_forty, y_values, 'o')
	# axes_forty.set_title('Velocity vs. Average Forty Minute Distance')

	# fig_one = plt.figure()
	# axes_one = fig_one.add_subplot(1, 1, 1)
	# axes_one.plot(x_one, y_values, 'o')
	# axes_one.set_title('Velocity vs. Average One Minute Distance')

	# fig_repmax = plt.figure()
	# axes_repmax = fig_repmax.add_subplot(1, 1, 1)
	# axes_repmax.plot(x_repmax, y_values, 'o')
	# axes_repmax.set_title('Velocity vs. Average Rep Max')

	# fig_watt = plt.figure()
	# axes_watt = fig_watt.add_subplot(1, 1, 1)
	# axes_watt.plot(x_watt, y_values, 'o')
	# axes_watt.set_title('Velocity vs. Average Max Watt')

	# fig_weight = plt.figure() 
	# axes_weight = fig_weight.add_subplot(1, 1, 1)
	# axes_weight.plot(x_weight, y_values, 'o')
	# axes_weight.set_title('Velocity vs. Average Weight')

	plt.show()

def main():
	rowerData = readRowerData('RowerInfo.csv')
	timeData = readTimeData('Data.csv')
	# print rowerData
	# print timeData
	plotData(rowerData, timeData)

main()
