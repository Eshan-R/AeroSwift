from amadeus import Client, ResponseError
import os

amadeus = Client(
    client_id = os.getenv("AMADEUS_CLIENT_ID"),
    client_secret = os.getenv("AMADEUS_CLIENT_SECRET"),
    hostname='test'
)

def search_flights(origin, destination, date, adults=1, children=0, infants=0):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults,
            children=children,
            infants=infants,
            currencyCode = "INR",
            max=10
        )
        return response.data
    except ResponseError as e:
        print("AMADEUS ERROR:", e)
        return []