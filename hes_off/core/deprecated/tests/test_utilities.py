## ------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------ ##
##                         ___   ___  ________    ________         ______    ________ ________                        ##
##                        |  |  |  | |   ____|   /       |        /  __  \  |   ____||   ____|                        ##
##                        |  |__|  | |  |__     |   (----` ______|  |  |  | |  |__   |  |__                           ##
##                        |   __   | |   __|     \   \    |______|  |  |  | |   __|  |   __|                          ##
##                        |  |  |  | |  |____.----)   |          |  `--'  | |  |     |  |                             ##
##                        |__|  |__| |_______|_______/            \______/  |__|     |__|                             ##
##                                                                                                                    ##
## ------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------ ##

# Import packages
import hes_off_object_oriented

## ------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------ ##


def test_read_configuration_file():
    IN = hes_off_object_oriented.read_configuration_file("test_file.cfg")
    assert IN["FLOAT_1"] == 1
    assert IN["FLOAT_2"] == 2
    assert IN["FLOAT_LIST"] == [1, 2, 3]
    assert IN["STRING_1"] == "HelloWorld"
    assert IN["STRING_2"] == "HelloWorld"
    assert IN["STRING_LIST"] == ["HelloWorld", "HelloWorld", "HelloWorld"]
    print(IN)


## ------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------ ##
## ------------------------------------------------------------------------------------------------------------------ ##


# Run the tests when this script is executed as main
if __name__ == '__main__':
    test_read_configuration_file()