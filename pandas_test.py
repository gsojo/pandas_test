import pandas as pd

def main():
    current = [
        {'Id': 20562, 'UserName': 'axr230', 'Email': 'ana.rodriguez@tdxgroup.com'},
        {'Id': 20986, 'UserName': 'axr231', 'Email': 'arun.raju@equifax.com'}
    ]

    input = [{'UserName': 'axr230', 'Email': 'james.hoskins@tdxgroup.com'}]


    current_df = pd.DataFrame.from_records(current)
    print('\nArcher Data:')
    print(current_df)
    input_df = pd.DataFrame.from_records(input)
    print('\nInput Data:')
    print(input_df)


    res = current_df.merge(
        input_df, how='right', on='UserName')
    print('\nMerged Data:')
    print(res)

if __name__ == '__main__':
    main()
