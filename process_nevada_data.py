from aggregate_data import sum_data, pivot_data

def process_clark_data(input_file, output_file, candidates):
    group_by = ['CountingGroup', 'PrecinctPortion']

    sum_data(infile=input_file, outfile='tmp.csv', group_by=group_by, vote_columns=candidates)
    pivot_data(infile='tmp.csv',
               outfile=output_file,
               vote_columns=candidates,
               group_by=group_by,
               index = 'PrecinctPortion',
               type_group = 'CountingGroup')


if __name__ == '__main__':
    pres_vote_columns = [
        "Harris, Kamala D.",
        "Oliver, Chase",
        "Skousen, Joel",
        "Trump, Donald J.",
        "None of These Candidates"
    ]
    process_clark_data(
        'Nevada/data/orig/clark_pres_2024.csv',
        output_file = 'Nevada/data/nv_clark_pres_2024_pivot.csv',
        candidates = pres_vote_columns)

    senate_vote_columns = [
        "Brown, Sam",
        "Cunningham, Chris",
        "Hansen, Janine",
        "Rosen, Jacky S.",
        "None of These Candidates"
    ]
    process_clark_data(
        'Nevada/data/orig/clark_senate_2024.csv',
        output_file = 'Nevada/data/nv_clark_senate_2024_pivot.csv',
        candidates = senate_vote_columns)
