def read_file(bestand,header):
    file = pd.read_table(bestand)
    print(file.head(10))
    # print(header)
    # print(file['sample'].head(10))
    # print(file[['protein_group', 'sample']])