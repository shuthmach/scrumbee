import pandas as pd
import re

def extract_matches(pattern, obj_to_search):
    ### This function takes a match pattern (assembled using re.compile) and an object to search (such as a Series or
    ### DataFrame column), returns a Series containing the matched items, and removes the matched items from the original
    ### object.
    
    matched_bool = obj_to_search.str.match(pattern)
    matched_str = obj_to_search[matched_bool]
    obj_to_search = obj_to_search.drop(obj_to_search[matched_bool].index)
    return matched_str, obj_to_search
