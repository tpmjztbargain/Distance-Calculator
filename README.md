# Distance Calculator

This Python script calculates the great-circle distance between two points on Earth, given their latitude and longitude coordinates.

## Features

- Uses the Haversine formula for accurate distance calculation over the Earth’s surface
- Simple command-line interface for user input
- Outputs the distance in kilometers

## Usage

1. **Run the script:**
   ```sh
   python distance_calculator.py
   ```

2. **Enter the latitude and longitude for both points when prompted.**

3. **The script will display the distance between the points in kilometers.**

## Example

```
Enter latitude and longitude for Point 1:
Latitude 1: 40.7128
Longitude 1: -74.0060

Enter latitude and longitude for Point 2:
Latitude 2: 34.0522
Longitude 2: -118.2437

Distance between points: 3935.75 km
```

## Formula

This script uses the Haversine formula:

```
a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlon/2)
c = 2 * asin(√a)
distance = R * c
```

Where:
- lat/lon are in radians
- R is the Earth's radius (6371 km)

## Requirements

- Python 3.x

No external dependencies are required.

## License

This project is licensed under the MIT License.
