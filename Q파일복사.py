##파일 복사하기

inFp, outFp=None,None
inStr,outStr="",""
inFname,outFname="",""

inFname=input("소스 파일명을 입력하세요: ")
inFp=open(inFname,"r")
outFname=input("타깃 파일명을 입력하세요: ")
outFp=open(outFname,"w")

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inList)

inFp.close()
outFp.close()
print("--",inFname,"파일이 ",outFname,"으로 정상적으로 복사됨--")
