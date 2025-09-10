import math

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great-circle distance between two points 
    on the Earth's surface using latitude and longitude.
    
    Parameters:
      lat1, lon1: Latitude and Longitude of point 1 (in decimal degrees)
      lat2, lon2: Latitude and Longitude of point 2 (in decimal degrees)
    
    Returns:
      Distance in kilometers
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)
    
    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    # Radius of Earth in kilometers. Use 6371 for km, 3956 for miles
    R = 6371
    
    distance = R * c
    return distance

if __name__ == "__main__":
    # Example usage
    print("Enter latitude and longitude for Point 1:")
    lat1 = float(input("Latitude 1: "))
    lon1 = float(input("Longitude 1: "))
    
    print("\nEnter latitude and longitude for Point 2:")
    lat2 = float(input("Latitude 2: "))
    lon2 = float(input("Longitude 2: "))
    
    distance = haversine(lat1, lon1, lat2, lon2)
    print(f"\nDistance between points: {distance:.2f} km")
