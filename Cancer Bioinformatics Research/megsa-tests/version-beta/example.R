###  The code for the MEGSA algorithm was developed by Dr. Xing Hua supported by the NIH intramural Research Program. 
###  Here we run analysis using TCGA LAML as an example. 
###  If you have questions, please send email to xing.hua@nih.gov or jianxin.shi@nih.gov. 
###  When reporting results, please cite Xing Hua et al., MEGSA: A powerful and flexible framework for analyzing mutual exclusivity of tumor mutations. 

################################################################################

source("MEGSA.R")

################################################################################

#Load the binary (1: mutation, 0: no mutation) mutation matrix from a text file.
#The first row has the gene names and the first column has the patient IDs.
#Example data: mutationMat_LAML.txt for TCGA LAML binary mutation data. 

mutationMat <- as.matrix(read.table("mutationMat_LAML.txt", header = TRUE, row.names = 1) != 0)

################################################################################

#First run permutations to generate the distribution of the maximum LRT statistic under the null hypothesis.
#nSimu: number of simulations (recommand 1000 or more, it may take ~ 10 hours for 1000 simulations).
#nPairStart: We first tested all pairs of genes and then pick up the top nPairStart gene pairs (ranked by P-values)
#            to perform multiple-path search to include more genes. Increasing nPairStart will slightly increase power 
#            but linearly increasing the computational time. Recommended nPairStart: (10, 30). 
#maxSize: the maximum size of putative MEGS.
maxSSimu <- funMaxSSimu(mutationMat, nSimu = 5, nPairStart = 10, maxSize = 2)


################################################################################

#Indentify significant MEGS
#level: the significance level or family-wise error after multiple testing correction based on permutations.
resultMEGSA <- funSelect(mutationMat, maxSSimu, level = 0.05)
str(resultMEGSA) #A list of 2 components (resultMEGSA$p: the global p value, resultMEGSA$MEGSList: a list of significant MEGS )

#MEGSList is the list of significant MEGS
MEGSList <- resultMEGSA$MEGSList
#Each MEGS has 4 attributes (S: LRT statistic; pNominal: nominal p value; pCorrected: multiple-testing corrected p value; coverage: the coverage of the MEGS)
str(MEGSList) 

################################################################################

#Convert the list of MEGS to a data frame and export it
MEGSDF <- funPrintMEGS(MEGSList, outputFile = "resultMEGS_LAML.txt")
print('m\n\n\n')

################################################################################

#Visualize the MEGS and generate the corresponding figures to a specify folder
#Current support "pdf", "png" and "jpg"
funPlotMEGS(MEGSList, mutationMat, outputDir = "figure_LAML", type = "pdf")
print('viz\n\n\n')

################################################################################

#Summarize the procedures above together
resultMEGSA <- funMEGSA("mutationMat_LAML.txt", "maxSSimu_LAML.txt", resultTableFile = "resultMEGSA_LAML.txt", figureDir = "figure_LAML")

################################################################################








