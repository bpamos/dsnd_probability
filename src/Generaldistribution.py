class Distribution:

    def __init__(self, mu=0, sigma=1):

        """ Generic distribution class for calculating and 
        visualizing a probability distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
            """
        
        self.mean = mu
        self.stdev = sigma
        self.data = []


    def read_data_file(self, data_name):
        """Function to read in data from a txt file or list. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.
        If list, the list should be all floats
                
        Args:
            data_name (string) or (list): if string it is the name of a file to read from
            if list, it is the list name

        Returns:
            None

        """
        if isinstance(data_name, list):
            self.data = data_name
        else:
            with open(data_name) as file:
                data_list = []
                line = file.readline()
                while line:
                    data_list.append(int(line))
                    line = file.readline()
            file.close()

            self.data = data_list