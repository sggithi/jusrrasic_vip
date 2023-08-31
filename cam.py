import argparse

def main():         
  parser = argparse .ArgumentParser() 
  parser .add_argument ('arg')
  args = parser .parse_args ()
  print(args)        

if __name__ == "__main__":
   main ()