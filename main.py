import argparse
def soll():
  print "This is the soll!"

def env():
  print "This is the env!"

def compare():
  print "This is the compare!"

def main():
  descStr = """
  This program compares the privileges between SOLL and ENV.
  """
  parser = argparse.ArgumentParser(description=descStr)

  parser.add_argument('--soll', action='store_true', required=False)

  parser.add_argument('--env', action='store_true', required=False)
  parser.add_argument('--compare', action='store_true', required=True)
  args = parser.parse_args()

  if args.soll:
    soll()
  if args.env:
    env()
  if args.compare:
    compare()

main()
