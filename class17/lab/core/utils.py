class Helper:
    def displayHelper(array):
        for item in array:
            try:
                item.display_info()
            except AttributeError:
                print(item)
            finally:
                print("==========")