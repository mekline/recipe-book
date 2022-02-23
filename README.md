# recipe-book
Compile a recipe book from submissions to a google form!

This code assumes you have a text format (TSV/CSV) version of recipe data called `recipes.tsv`. I created this by having people enter recipes into a google form.  If people follow a request to do things like number each step in a recipe on its own line, you're in business! The key to getting this working well-enough was to separate the ingredients and instructions into two separate boxes. But anyhow, expect to still do manual formatting to clean/match styles once you have compiled everything, and add in the recipes of people who sent you photographs of newspaper clippings :)

The general workflow is to convert the TSV -> html -> word document -> pdf.  The html-> word conversion is performed just by forcing Word to open the html file, and there is probably a better way to create a PDF than that! Oh well!
