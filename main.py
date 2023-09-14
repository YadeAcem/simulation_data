import pandas as pb

def read_file(file):
    df = pb.read_excel(file)
    print(df)


if __name__ == '__main__':
    simulation_data = 'Simulation_HeartProteomics_20230914.xlsx'
    read_file(simulation_data)