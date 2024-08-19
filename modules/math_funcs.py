import datetime

class MathFuncs:
    def __init__(self) -> None:
        pass

    def calculate_mean_average(self, numbers: list) -> float:
        """
        Calculate the mean average of a list of numbers
        """
        return round(sum(numbers) / len(numbers), 2)
    
    def calculate_mode_average(self, numbers: list) -> float:
        """
        Calculate the mode average of a list of numbers
        """
        return max(set(numbers), key=numbers.count)
    
    def round_cordinates(self, cordinate_value: float) -> float:
        """
        Rounds Latitude or Longitude to 2 decimal places
        """
        return round(cordinate_value, 2)
    
    def convert_epoch_to_date(self, epoch: int) -> str:
        """
        Converts Epoch to Date
        """
        parsed_epoch = datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')
        return parsed_epoch
    
    def calculate_median_average(self, numbers: list) -> float:
        """
        Calculate the median average of a list of numbers
        """
        pass


    