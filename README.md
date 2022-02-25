# recipe-book
Compile a recipe book from submissions to a google form!

This code assumes you have a text format (TSV/CSV) version of recipe data called `recipes.tsv` (.gitignored here in case anyone doesn't want their recipes on the open internet.)

I created this by having people enter recipes into a google form.  With separate fields for (at least) ingredients and instructions and a pre-filled link with examples of numbering/bullets, this results in decently structured data that is not too onerous to use as a base for further beautification. But anyhow, expect to still do manual formatting to clean/match styles once you have compiled everything, and add in the recipes of people who sent you photographs of newspaper clippings :) (Or yourself. Don't forget your own recipe, if you are the recipe compiler!)

The general workflow is to convert the TSV -> html -> pdf. Previously I forced Word to open html then saved as PDF, but that no longer worked in 2022.  LibreOffice to the rescue!
