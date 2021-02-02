# Project Overview

### This is a concise repository for [The Epistasis project codes](https://gitlab.com/cansuyalcin/projects_portfolio/-/tree/master/Cancer%20Bioinformatics%20Research "Research"). The codes can be found in the [link](https://gitlab.com/cansuyalcin/projects_portfolio/-/tree/master/Cancer%20Bioinformatics%20Research "Research")

### In this project we experimented with many ideas, factors and parameters. A lot of them are not relevant for the final paper. This version of the project contains the latest analyzes made so far. 

### The project involves evaluation of mutual exclusivity methods: Discover, Discover_strat, Fisher's Exact Test, MEGSA, MEMO and WExT. The results from these methods include pairwise mutual exclusivity p-values. Based on them, we apply our network centric epistatic evaluation.

# Structure of the Project

#### 1. mutex_data: Includes all the input data such as mutual_exclusivity files, MLA files, PPI files etc. "{method}_mutation_filtered_ep_data" folder contains the MEX files.

	A. binary_matrices_all_genes_ep_mutation_filtered: includes binary matrices for mutation data.

	B. {method}_mutation_filtered_ep_data: inlcudes pairwise mutual exclusivity p-values.

	C. molecular_strat_patient_list: includes patient and subtype information for BRCA and COADREAD molecular stratification.

	D. MLA_ep_mutation_filtered_all_genes: Corresponding MLA.

	E. rare_genes: 2% or 3% rare genes.

	F: Census_allFri_Apr_26_12_49_57_2019.tsv: COSMIC file (Known driver genes)


#### 2. src_main: this includes the source code for the proposed evaluation and additional analysis

	A. evaluate_methods_on_permutations_version3_with_case_counts_rare.ipynb is the main source code for the evaluation. As output, you get tables with all analysis results.

	B. prep_table_for_latex.ipynb takes the evaluation results (A) and preps the result in Latex format. It is convenient for creating tables (check main paper and supplementary table formats, some &s may need to be removed).

	C. perc_sig_all_comb_rare.ipynb computes genewise percentage significance and save the file. I separated this since it takes a long time for t5. Relevant for plotting non-randomized plots quickly.

	D. plot_perc_sig_fig3_random_sampling_neighbors.ipynb takes the mutex files as input, and plots %sig.

	E. Analyzes is a file that contains necessary analyzes and tests which gave us an idea of data. 
		It contains such files:
		1.hypergeometric_test.ipynb which performs hypergeometric test on COADREAD t20 data,
		2.Mut_freq_no_neighbors.ipynb that outputs the percentage significant findings, mutual frequency and number of neighbors of each CGC genes,
		3.plot_perc_sig_fig3_random_sampling_neighbors_excluding_one_neighbors.ipynb is the adapted version of the main code. It gives an output of percentage significant plots for the genes have more than one neighbors,
		4.evaluate_methods_on_permutations_version3_with_case_counts_rare_TSN_networks.ipynb which performs NCEE algorithm on Tissue-Specific Networks (TSN)

	F.version ziv - GTEx TSN analysis: This file contains tissue spesific network analysis on each cancer type. 

#### 3. results_main: This contains the results from the scripts in src_main.

#### 4. out: This contains outputs from the scripts in Analyzes. 

