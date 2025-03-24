import pandas as pd

def sum_data(infile, outfile, group_by, vote_columns):
    """
    Aggregate election data based on specified columns and groupings.

    :param infile: Input CSV file with election data
    :param outfile: Output CSV file to save the aggregated data
    :param group_by: List of columns to group by
    :param vote_columns: List of columns corresponding to the presidential candidates
    """
    # Read the input CSV file
    df = pd.read_csv(infile)

    df[vote_columns] = df[vote_columns].apply(pd.to_numeric, errors='coerce')

    # Group the data by specified columns and sum the vote columns
    grouped_votes = df.groupby(group_by)[vote_columns].sum().reset_index()

    # Save the aggregated data to the output CSV file
    grouped_votes.to_csv(outfile, index=False)


def pivot_data(infile, outfile, vote_columns, group_by, index, type_group):
    """
    Pivot election data based on specified columns and groupings.

    :param infile: Input CSV file with aggregated data
    :param outfile: Output CSV file to save the pivoted data
    :param vote_columns: List of columns corresponding to the candidates
    :param group_by: List of columns to group by
    """
    # Read the input CSV file
    df = pd.read_csv(infile)

    df[vote_columns] = df[vote_columns].apply(pd.to_numeric, errors='coerce')

    # Group by PrecinctPortion and CountingGroup (which represents the vote type)
    grouped = df.groupby(group_by)[vote_columns].sum().reset_index()

    # Melt the data to long format so each row is a candidate vote record
    melted = grouped.melt(id_vars=group_by,
        value_vars=vote_columns,
        var_name='Candidate',
        value_name='Votes')

    # Create a combined column for Candidate and vote type.
    # This example extracts only the first name from the candidate field for a cleaner column name,
    # change this as needed to suit your naming preference.
    melted['Candidate_VoteType'] = melted['Candidate'].str.split(',').str[0] + ' ' + melted['CountingGroup']

    # Pivot the table so that each precinct is a row and each candidate-vote type combination is a column.
    pivoted = melted.pivot_table(index=index,
                             columns='Candidate_VoteType',
                             values='Votes',
                             fill_value=0).reset_index()
    # Save the pivoted data to the output CSV file
    pivoted.to_csv(outfile, index=False)