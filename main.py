#Interval finder
#Example: start = 10, end = 16, intervals = 5, output: [11.0,12.0,13.0,14.0,15.0]

start = 10
end = 200
intervals = 5
output = []

diff = (end-start)
iterator = diff/(intervals+1)

for n in range(intervals):
  start = round(start+iterator,1)
  output.append(start)

print(output)
