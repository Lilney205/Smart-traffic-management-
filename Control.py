import time

class TrafficLight:
    def __init__(self):
        self.state = "RED"

    def change_state(self, car_count):
        if car_count > 5:
            self.state = "GREEN"
        else:
            self.state = "RED"

    def get_state(self):
        return self.state

if __name__ == "__main__":
    traffic_light = TrafficLight()
    
    for car_count in range(10):  # Simulate traffic changes
        traffic_light.change_state(car_count)
        print(f"Car Count: {car_count} | Traffic Light: {traffic_light.get_state()}")
        time.sleep(1)
