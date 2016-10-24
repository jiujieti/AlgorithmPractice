import argparse
def excel():
  print "This is the excel!"

def env():
  print "This is the database!"

def compare():
  print "This is the comparison!"

def main():
  descStr = """
  This program compares the excel file with the database
  """
  parser = argparse.ArgumentParser(description=descStr)

  parser.add_argument('--excel', action='store_true', required=False)
  parser.add_argument('--env', action='store_true', required=False)
  parser.add_argument('--compare', action='store_true', required=True)

  args = parser.parse_args()

  if args.excel:
    excel()
  if args.env:
    env()
  if args.compare:
    compare()

main()
