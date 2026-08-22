import numpy as np



def create_1D_Array():
    print("### 1-D Array Creation ###\n")

    array_from_list = np.array([10,20,30,40,50])
    print(f"1. Array from list :{array_from_list}")
    print(f"Shape: {array_from_list.shape}")
    print(f"Data Type: {array_from_list.dtype}")
    print(f"Size: {array_from_list.size}\n")

    array_from_arange = np.array([0,20,3])
    print(f"2. Array from arange: {array_from_arange}")
    print(f"The Dimention: {array_from_list.ndim}\n")

    array_1_d ={"from_list":array_from_list,
                "from_arange":array_from_arange}
    return array_1_d


def main():
    """
    Main function to execute all Numpy concepts

    return: None 
    """
    array_id = create_1D_Array()

if __name__ == "__main__":
    """
    Program Entry Point
    This block ensure that the main() function is executed only when this script is run directly , not when imported as modul
    """
    main()
    
