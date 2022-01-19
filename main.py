if __name__ == '__main__':
    from realestate_com_au import RealestateComAu
    import pandas as pd

    api = RealestateComAu()

    # Get property listings
    listings = api.search(locations=["vic"], channel="buy")

    df = pd.DataFrame(listings)

    df.to_csv('realestate_listings.csv', index=False)
