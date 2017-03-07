<h3>add_codes_to_SSM</h3>

<p>
add_codes_to_SSM.py accepts two arguments: the first is the path to an SSM JSON
file (see https://github.com/steve9000gi/ssm) and the second is the path to the
related CBLM file (see https://github.com/steve9000gi/AddCodesToBLM). It reads 
in the two files, finds the code associated with each SSM node from the CBLM,
adds that code to the corresponding node in the SSM as a new key/value pair, and
writes the updated JSON object to a file.
</p>
