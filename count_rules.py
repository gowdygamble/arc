import glob 

rule_files = 'rules/rules/*.py'

rfs = glob.glob(rule_files)
print(len(rfs))