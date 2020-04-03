test_data = ['5', '6', '7', '6', '5', '4', '5', '6', '7', '8', '9', '8', '7', '6', '7', '8', '9']


# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of
# appearance in the original data.


def main():
    master_dict = peaks_and_valleys(test_data)
    return f"Data: {master_dict['data']} \nIndex: {master_dict['index_list']} \nPeaksAndValleys: {master_dict['peaks_and_valleys']}"

def peaks(list_data):
    peaks_dict = dict()
    for idx, val in enumerate(list_data):
        if len(list_data) - 1 > idx > 0:
            if list_data[idx-1] < val > list_data[idx+1]:
                peaks_dict[str(idx)] = val
                print('Peak found ', peaks_dict[str(idx)])

    print('peak list is ', peaks_dict)
    return peaks_dict


def valleys(list_data):
    valley_list = dict()
    for idx, val in enumerate(list_data):
        if len(list_data) - 1 > idx > 0:
            if list_data[idx - 1] > val < list_data[idx + 1]:
                valley_list[str(idx)] = val
                print('Peak found ', valley_list[str(idx)])

    print('peak list is ', valley_list)
    return valley_list


def peaks_and_valleys(sample_data):
    # Convert items in list to integers

    # try:
        # for i in range(0, len(sample_data)):
        #     sample_data[i] = int(sample_data[i])

    parsed_list = list(map(int, sample_data))
    # except ValueError:
    #     return 'Invalid sample data given'

    # Create dictionary of peaks with key: index, value: value
    peaks_dict = peaks(parsed_list)
    sorted(peaks_dict.keys())

    # Create dictionary of valleys with key: index, value: value
    valleys_list = valleys(parsed_list)
    sorted(valleys_list.keys())

    # Create list of all indexes of sample_data 0 to -N1
    index_list = list()
    for i in range(0, len(sample_data)):
        index_list.append(i)

    # Create list of peaks and valleys ordered numerically by index
    p_o_v_indexes = list()
    for key, val in peaks_dict.items():
        p_o_v_indexes

    master_dict = {"data" : sample_data, "index_list": index_list, "peaks_and_valleys": p_o_v_indexes}
    return master_dict
