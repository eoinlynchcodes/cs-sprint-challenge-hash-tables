def get_indices_of_item_weights(weights, length, limit):

    weight_dict = {}

    for index, weight in enumerate(weights):
        complement = limit - weight
        if complement in weight_dict:
            return [index, weight_dict[complement]]
        else: 
            weight_dict[weight] = index


print(get_indices_of_item_weights([1,2,3], 3, 3))



    # get the value in weights
    # put it into the weight_dict
    # check if the contents of weight_dict - weight = limit
    # if it does, return weight_dict, weight