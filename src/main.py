import matplotlib.pyplot as plt
import pandas

def get_csv_data(filepath: str) -> list:
	data = []
	try:
		data = pandas.read_csv(filepath)
		
	except Exception as e:
		print(e)
	else:
		print("You copied %d lines to in-memory"%( len(data) ))
	finally:
		print()

	return data

def process_data(src_list:[str])-> [int]:
	res = []
	cur = 0

	for e in src_list:
		if e == "+":
			cur += 1
		elif e == "-":
			cur -= 1
		elif e == "=":
			pass
		else:
			raise Exception("unexpected character in sentiment column")

		res.append(cur)

	return res 


def main():

	data = get_csv_data("Life Graph Data - Sheet1.csv")

	# x axis values
	x = data.date.values

	# corresponding y axis values
	y = process_data(data.sentiment.values)
	  
	# plotting the points 
	plt.plot(x, y)
	  
	# naming the x axis
	plt.xlabel('x - axis: Date')
	# naming the y axis
	plt.ylabel('y - axis: Happiness')
	  
	# giving a title to my graph
	plt.title('Happiness vs. Time')
	  
	# function to show the plot
	plt.show()


if __name__ == "__main__":
	main()

