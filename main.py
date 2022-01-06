if __name__ == '__main__':
    from realestate_com_au import RealestateComAu

    api = RealestateComAu()

    # Get property listings
    listings = api.search(locations=["3205"], channel="buy", keywords=[
                          "tenant"], exclude_keywords=["pool"])
    print(listings)
