import os
import pandas as pd

def get_meta_info(file):
    """
    Function used to load data from a csv file with metadata
    
    :param file: the csv file containg metadata
    :return: dataframe containing data from the csv file
    """
    
    df = pd.read_csv(file)
    
    return df

def rename_samples(file):
    """
    Function used to rename samples for MultiQC analysis.
    It saves the old names and the new names to a tsv file, 
    which will serve as instructions for renaming.
    
    :param file: csv file containg metadata 
    """
    
    # load metadata from a csv file
    df = get_meta_info(file)
    
    directory = "../data/"
    
    data = []

    # for every file
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            subdf = df[df["probka"] == filename.split(".")[1]]
            elements = filename.split(".")
            name = "{}.{}".format(elements[1], elements[2])
            data.append([filename.replace(".fastq", ""), name])
    
    df_output = pd.DataFrame(data)
    
    df_output.to_csv("../rename_samples.tsv", sep="\t", header=None, index=False)
    

def create_instruction_file(file):
    """
    Function used to instruct the import of files into the QIIME program.  
    It writes to a csv file the ID of the sample, the path to the forward 
    and reverse read file for that sample, and the read direction information.
    
    :param file: csv file containg metadata
    """
    
    #  load metadata from a csv file
    df = get_meta_info(file)
    
    directory = "../data/"
    
    data = []
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            type = filename.split(".")[-2]
            subdf = df[df["probka"] == filename.split(".")[1]]
            name = "{}_{}_{}".format(subdf["zbiornik"].values[0], subdf["rok"].values[0], subdf["pora_roku"].values[0])
            dir = "$PWD/data/{}".format(filename)
            if type == "1":
                data.append([filename.split(".")[1], dir, "forward"])
            if type == "2":
                data.append([filename.split(".")[1], dir, "reverse"])
    
    df_output = pd.DataFrame(data, columns=["sample-id", "absolute-filepath", "direction"]).sort_values(["sample-id"])
    
    df_output.to_csv("../seqs_import.csv", index=False)
    

def create_metadata(file):
    """
    Function used to create a tsv file with metadata about the analyzed samples.  
    It saves the data to a tsv file that contains information about the sample ID 
    and name, reservoir name, season, year and region.
    
    :param file: csv file containg metadata
    """
    
    df = get_meta_info(file)
    directory = "../data/"
    data = [["#q2:types", "categorical", "categorical", "categorical", "categorical", "categorical"]]
    visited = []
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            # sample id
            name = filename.split(".")[1]
            if name not in visited:
                subdf = df[df["probka"] == name]
                # all values for the sample
                values = subdf.values[0].tolist()
                new_list = values
                # data to the metadata file
                new_list.insert(0, values[0])
                data.append(new_list)
            visited.append(name)
    
    df_output = pd.DataFrame(data, columns=["#SampleID", "probka", "zbiornik", "pora_roku", "rok", "region"])
    df_output.to_csv("../metadata.tsv", sep="\t", index=False)

                
def main():
    
    file = "../samples.csv"
    rename_samples(file)
    create_instruction_file(file)
    create_metadata(file)


if __name__ == "__main__":
    main()