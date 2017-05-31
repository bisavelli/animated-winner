import yaml
import jinja2
import os 
import sys
import argparse
from bracket_expansion import bracket_expansion

def main():

	parser = argparse.ArgumentParser(description='Script requires all variables to run.')
	parser.add_argument('target_device', action='store', type=str)
	parser.add_argument('template', action='store', type=str)
	#Print the processed arguments for troubleshooting purposes
	print(parser.parse_args())

	TEMPLATE_FILENAME = sys.argv[2]
	HOST_INFORMATION = sys.argv[1]

	#loader object to read template config files
	#env object created to interact with template and formatting options
	loader = jinja2.FileSystemLoader(searchpath='./templates')
	ENV = jinja2.Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

	#you can also use filters to expand the jinja funtionality
	ENV.filters['bracket_expansion'] = bracket_expansion

	#Use this to read from yaml file from 'hosts' directory to populate the template
	with open('hosts/' + HOST_INFORMATION + '_vars.yaml') as _:
		varfile = yaml.load(_)
	template = ENV.get_template(TEMPLATE_FILENAME + '.j2')

	with open(sys.argv[1] + '.cfg', "w") as file:
		file.write(template.render(config = varfile))


# ...

if __name__ == "__main__":
	main()



