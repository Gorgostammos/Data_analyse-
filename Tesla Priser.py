import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'tesla_stock.csv'
dates,highs = [], []

# Open the file and read inside the with block
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # Skip the header row

    # Read the rows and store the 'high' values
    for row in reader:
        current_date=datetime.strptime(row[0],'%Y-%m-%d')
        high = float(row[2])  # Convert to float since it's a decimal value
        dates.append(current_date)
        highs.append(high)

# Now plot the graph after filling the 'highs' list
#plt.style.use('ggplot')
fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.plot(dates,highs, c='red')

ax.set_title("Tesla priser", fontsize=24)
ax.set_xlabel("år", fontsize=14)
ax.set_ylabel("priser", fontsize=14)

ax.tick_params(axis='both',which='major' ,labelsize=14)
plt.show()

print(highs)
