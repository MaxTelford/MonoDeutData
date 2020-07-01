GITHUBREPO: Lack of support for Deuterostomia prompts reinterpretation of the first Bilateria
=============================================================================================
​
This is the GITHUBREPO for the publication Kapli _et al_ "Lack of support for Deuterostomia prompts reinterpretation of the first Bilateria" ([DOI.XXX](https://doi.XXX)). It contains all the `Trees`, `Scripts` and `Simulation_data` used in the study. If you require further materials or information please contact m.telford@ucl.ac.uk.
​
​
---
​
Trees
-----
​
In the methods sections **_Measuring support for deuterostome and protostome branches_** and **_Support for monophyletic versus paraphyletic deuterostomes and protostomes_** we generated classic trees, alternate trees and collpsed trees. Each dataset (`Cannon`, `Laumer`, `Marletaz`, `Rouse`, `Philippe`) has the following:
​
 * `<dataset>_Classic_Tree.tre`
​
		((Lophotrochozoa,Ecdysozoa),(Xenambulacraria,Chordata))  
 * `<dataset>_Alt_Tree_D1.tre`
​
		(Chordata,(Xenambulacraria,(Lophotrochozoa,Ecdysozoa)))
 * `<dataset>_Alt_Tree_D2.tre`
​
		(Xenambulacraria,(Chordata,(Lophotrochozoa,Ecdysozoa)))
 * `<dataset>_Alt_Tree_P1.tre`
​
		(Ecdysozoa,(Lophotrochozoa,(Xenambulacraria,Chordata)))
 * `<dataset>_Alt_Tree_P2.tre`
​
		(Lophotrochozoa,(Ecdysozoa,(Xenambulacraria,Chordata)))
 * `<dataset>_Classic_Tree_collapse_deut.tre`
​
		((Lophotrochozoa,Ecdysozoa),Ambulacraria,Chordata)
 * `<dataset>_Classic_Tree_collapse_proto.tre`
​
		(Lophotrochozoa,Ecdysozoa,(Ambulacraria,Chordata)) 
​
      
​
---
​
​
Scripts
-------
​
For the comparison of likelihoods from three alternative tree hypotheses we used the following scrips. For usage see in the scripts.
​
 * `likelihood_transform.py` - was used to transform likelihood values.
 * `plot_triangles.R` - was used to plot the transformed likelihoods. CSV inputs used are provided in the supplementary material.
​
---
​
Simulation_data
---------------
​
This folder contains the sub-folders `empirical_alignments`, `guide_trees` and `simulation_results` from the methods sections **_Measuring branch lengths with different models and model fitness_** and **_Simulations - Systematic Error_**
​
 * `empirical_alignments`
	1. `metazoa_UPhO_d0.5.phylip.subset36.JACK50K.fasta` - the 50K "reduced-Laumer" alignment.
	2. `metazoa_UPhO_d0.5.phylip.subset36.JACK10K.fasta` - the further reduced 10K version of the "reduced-Laumer" alignment.
​
 * `guide_trees`
	1. `Classic_tree.txt_metazoa_UPhO_d0.5.phylip.subset36…CK50K.fasta.tree`
​
			((Lophotrochozoa,Ecdysozoa),(Xenambulacraria,Chordata))  
	2. `Alt_Tree_D1_metazoa_UPhO_d0.5.phylip.subset36.JACK50K.fasta.tree`
		
			(Chordata,(Xenambulacraria,(Lophotrochozoa,Ecdysozoa)))  
	3. `Alt_Tree_D2_metazoa_UPhO_d0.5.phylip.subset36.JACK50K.fasta.tree`
​
			(Xenambulacraria,(Chordata,(Lophotrochozoa,Ecdysozoa)))  
​
 * `simulation_results` - all results for 50k and 10k alignments, with all taxa and with long/short branches removed.
