import csv


def generateFiles(input_file):
    # Write your code here
    class OrderDetail:
        def __init__(self, totalQuantity, brand):
            self.totalQuantity = totalQuantity
            self.brandsDict = dict()
            if brand not in self.brandsDict:
                self.brandsDict[brand] = 1
            else:
                self.brandsDict[brand] += 1

    with open('{}'.format(input_file)) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        orders = dict()
        orderTotal = 0
        for row in readCSV:
            productName = row[2]
            orderQuantity = int(row[3])
            brand = row[4]
            orderTotal += 1
            if productName not in orders:
                orders[productName] = OrderDetail(orderQuantity, brand)
            else:
                orders[productName].totalQuantity += orderQuantity
    csvfile.close()

    for product, orderDetail in orders.items():
        with open('0_{}'.format(input_file), mode='a') as output_0:
            output_0 = csv.writer(output_0, delimiter=',',
                                  quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_0.writerow(
                [product, '{:2f}'orderDetail.totalQuantity / orderTotal])

        with open('1_{}'.format(input_file), mode='a') as output_1:
            output_1 = csv.writer(output_1, delimiter=',',
                                  quotechar='"', quoting=csv.QUOTE_MINIMAL)
            orderedBrands = orderDetail.brandsDict
            popularBrand = max(
                orderedBrands, key=lambda key: orderedBrands[key])
            output_1.writerow([product, popularBrand])


if __name__ == '__main__':
    input_file = input()
    generateFiles(input_file)
`
