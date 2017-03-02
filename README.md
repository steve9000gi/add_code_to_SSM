<h3>add_code_to_SSM</h3>

<p>
add_code_to_SSM.py accepts two arguments: the first is the path to an SSM JSON
file (see https://github.com/steve9000gi/ssm) and the second is the path to the
related CBLM file (see https://github.com/steve9000gi/AddCodesToBLM). It reads 
in the two files, finds the code associated with each SSM node from the CBLM,
adds the code to the SSM as a new key/value pair, and writes the updated JSON
object to a file.
</p>
