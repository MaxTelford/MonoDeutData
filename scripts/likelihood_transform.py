import sys
import math


'''
Example usage:
    
python likelihood_transform.py CTIQ_Results.txt D1IQ_Results.txt D2IQ_Results.txt 

'''


likelihood_file_1 = open(sys.argv[1], "r")
likelihood_file_2 = open(sys.argv[2], "r")
likelihood_file_3 = open(sys.argv[3], "r")


likelihood_file_1_lines = [x.strip().split() for x in likelihood_file_1.readlines()]
likelihood_file_2_lines = [x.strip().split() for x in likelihood_file_2.readlines()]
likelihood_file_3_lines = [x.strip().split() for x in likelihood_file_3.readlines()]

likelihood_triplets = []

for i in range(len(likelihood_file_1_lines)):
    likelihood_triplets.append([likelihood_file_1_lines[i][0][:-1],
                                float(likelihood_file_1_lines[i][1]),
                                float(likelihood_file_2_lines[i][1]),
                                float(likelihood_file_3_lines[i][1])
                                ])


likelihood_triplets_transformed = []

for entry in likelihood_triplets:
    likelihood_1 = entry[1]
    likelihood_2 = entry[2]
    likelihood_3 = entry[3]
    
    likelihood_0 = max(likelihood_1, likelihood_2, likelihood_3)
    
    transformed_likelihood_1 = math.e ** (likelihood_1 - likelihood_0)
    transformed_likelihood_2 = math.e ** (likelihood_2 - likelihood_0)
    transformed_likelihood_3 = math.e ** (likelihood_3 - likelihood_0)
    
    total = transformed_likelihood_1 + transformed_likelihood_2 + transformed_likelihood_3
    
    
    
    likelihood_triplets_transformed.append([entry[0],
                                            round(transformed_likelihood_1/total, 7),
                                            round(transformed_likelihood_2/total, 7),
                                            1 - (round(transformed_likelihood_1/total, 7) + round(transformed_likelihood_2/total, 7))
                                            ])
    
result = {"T1": [],
          "T2": [],
          "T3": [],
          "T12": [],
          "T23": [],
          "T13": [],
          "T123": []
}    

labels = {}   
counter_of_anomalous = 0
 
for point in likelihood_triplets_transformed:
    gene_name = point[0]
    L1 = point[1]
    L2 = point[2]
    L3 = point[3]
    
    valid_groups = []
    
    if (L1 >= 0.666666666666666) and (L2 <= 0.333333333333) and (L3 <= 0.333333333333):
        result["T1"].append(gene_name)
        valid_groups.append("T1")
        labels[gene_name] = "T1"
        
    if (L1 <= 0.333333333333) and (L2 >= 0.66666666666666) and (L3 <= 0.333333333333):
        result["T2"].append(gene_name)
        valid_groups.append("T2")
        labels[gene_name] = "T2"
    if (L1 <= 0.333333333333) and (L2 <= 0.333333333333) and (L3 >= 0.66666666666666):
        result["T3"].append(gene_name)
        valid_groups.append("T3")
        labels[gene_name] = "T3"
        
    if (L1 > 0.25 and L1 < 0.66666666666666) and (L2 > 0.25 and L2 < 0.666666666666666) and (L3 < 0.1666666666):
        result["T12"].append(gene_name)
        valid_groups.append("T12")
        labels[gene_name] = "T12"
    if (L1 < 0.6666666666666666666) and (L2 < 0.25) and (L3 < 0.1666666666):
        result["T12"].append(gene_name)
        valid_groups.append("12")
        labels[gene_name] = "T12"
    if (L1 < 0.25) and (L2 < 0.6666666666666666666) and (L3 < 0.1666666666):
        result["T12"].append(gene_name)
        valid_groups.append("12")
        labels[gene_name] = "T12"
        
        
    if (L1 < 0.1666666666) and (L2 > 0.25 and L2 < 0.66666666666666) and (L3 > 0.25 and L3 < 0.666666666666666):
        result["T23"].append([gene_name, L1, L2, L3])
        valid_groups.append("T23")
        labels[gene_name] = "T23"
    if (L1 < 0.1666666666) and (L2 < 0.6666666666666666666) and (L3 < 0.25):
        result["T23"].append(gene_name)
        valid_groups.append("23")
        labels[gene_name] = "T23"
    if (L1 < 0.1666666666) and (L2 < 0.25) and (L3 < 0.6666666666666666666):
        result["T23"].append(gene_name)
        valid_groups.append("23")
        labels[gene_name] = "T23"
        
    if (L1 > 0.25 and L1 < 0.666666666666666) and (L2 < 0.1666666666) and (L3 > 0.25 and L3 < 0.66666666666666):
        result["T13"].append(gene_name)
        valid_groups.append("T13")
        labels[gene_name] = "T13"        
    if (L1 < 0.6666666666666666666) and (L2 < 0.1666666666) and (L3 < 0.25):
        result["T13"].append(gene_name)
        valid_groups.append("13")
        labels[gene_name] = "T13"
    if (L1 < 0.25) and (L2 < 0.1666666666) and (L3 < 0.6666666666666666666):
        result["T13"].append(gene_name)
        valid_groups.append("13")
        labels[gene_name] = "T13"
        
    if (L1 < 0.6666666666666666666) and (L2 < 0.6666666666666666666) and (L3 < 0.6666666666666666666) and (L1 > 0.1666666666) and (L2 > 0.1666666666) and (L3 > 0.1666666666):
        result["T123"].append(gene_name)
        valid_groups.append("T123")
        labels[gene_name] = "T123"
       
    if (len(valid_groups) != 1):
        print(gene_name, L1, L2, L3, valid_groups)
        counter_of_anomalous += 1
        
               
print("\n")    
print("Total number of input genes: " + str(len(likelihood_triplets_transformed)))
print("\n")
print("Genes in T1: " + str(len(result["T1"])))
print("Genes in T2: " + str(len(result["T2"])))
print("Genes in T3: " + str(len(result["T3"])))
print("Genes in T12: " + str(len(result["T12"])))
print("Genes in T23: " + str(len(result["T23"])))
print("Genes in T13: " + str(len(result["T13"])))
print("Genes in T123: " + str(len(result["T123"])))

print("\n")
print("Final sum of genes: " + str(len(result["T1"]) + len(result["T2"]) + len(result["T3"]) + len(result["T12"]) + len(result["T23"]) + len(result["T13"]) + len(result["T123"])))
print("Number of genes in more than one compartments: " + str(counter_of_anomalous))    
print("\n")
print("\n")

'''
for entry in likelihood_triplets_transformed:
    print("================================================")
    print("Gene ID: " + entry[0])
    print("(" + str(entry[1]) + "," + str(entry[2]) + "," + str(entry[3]) + ")")
'''

output = open("triplets.tsv", "w")

for point in likelihood_triplets_transformed:
    gene_name = point[0]
    L1 = point[1]
    L2 = point[2]
    L3 = point[3]
    
    output.write(gene_name + "\t" + str(L1) + "\t" + str(L2) + "\t" + str(L3) + "\t" + labels[gene_name] + "\n" )
    