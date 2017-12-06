# Import pandas
import pandas as pd

# Define count_entries()
def count_entries(df, col_name):
    """Return a dictionary with counts of 
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}
    
    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] += 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return(langs_count)

# Define count_entries()
def count_entries_2(df, col_name = "lang"):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]
    
    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count

def count_entries_3(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    
    # Iterate over column names in args
    for col_name in args:
    
        # Extract column from DataFrame: col
        col = df[col_name]
    
        # Iterate over the column in DataFrame
        for entry in col:
    
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
    
            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count



    
# Import Twitter data as DataFrame: df
tweets_df = pd.read_csv("tweets.csv")

# Call count_entries(): result
result = count_entries(tweets_df, 'lang')

# Print the result
print(result)

# Call count_entries_2(): result1
result1 = count_entries_2(tweets_df)

# Call count_entries_2(): result2
result2 = count_entries_2(tweets_df, "source")

# Call count_entries_3(): result1
result1 = count_entries_3(tweets_df, 'lang')

# Call count_entries_3(): result2
result2 = count_entries_3(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)
