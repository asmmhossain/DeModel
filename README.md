# DeModel
Pipeline for selecting/rejecting demographic model on molecular data. The pipeline will except dated molecular sequence data preferably in fasta format and a date file.

The pipeline will implement the following steps:
  - Align sequences (*e.g.* Muscle)
  - Reconstruct phylogeny (*e.g.* ExaML)
  - Root and clockify tree (*e.g.* LSD)
  - Fit demographic model on to the tree
