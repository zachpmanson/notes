
Pandas is an incredible tool! Especially for data exploration. Sadly it does not allow type validation, making is difficult to ascertain what are inside `pd.DataFrame` objects outside of using a debugger. Remember, [[Command Click]]. When pandas transformations are needed, try to limit how much a single dataframe gets passed around, ideally keeping its entire existence within a single function with type information for the input and outputs. This will allow future developers to easily figure out what is in the dataframe. Sometimes passing a dataframe through multiple functions will be unavoidable, that's okay! Just be aware.

If you are passing a dataframe to a function, its a good idea to add a check on what columns are expected to exist. This should [[fail loudly]]. 
