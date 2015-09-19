import dryscrape

if __name__ == '__main__':
    my_url = "http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8C%97%E4%BA%AC&searchArrivalAirport=%E4%B8%8A%E6%B5%B7&searchDepartureTime=2015-09-21&searchArrivalTime=2015-10-11&nextNDays=0&startSearch=true&fromCode=BJS&toCode=SHA&from=zdzl&lowestPrice=null"
    session = dryscrape.Session()
    session.visit(my_url)
    response = session.body()
    print response
