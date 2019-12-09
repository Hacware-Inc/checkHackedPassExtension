import json


FILENAME = '../data/PwnedPasswordsTop100k.txt'
FILENAME_JSON = '../data/PwnedPassDict.json'

def main():
   # outJson.write("[")
   # outJson.write("\n")
   with open(FILENAME) as fp:
      line = fp.readline()
      cnt = 1
      outJson = open(FILENAME_JSON, "a")
      #outJson.write("[")
      outJson.write("{")
      while line:
           print("Line {}: {}".format(cnt, line.strip()))
           outJson.write("\""+str(line.strip())+"\": true,")
           line = fp.readline()
           cnt += 1
      #outJson.write("]")
      outJson.write("}")
      outJson.close()
      fp.close();


if __name__ == '__main__':
    main()    