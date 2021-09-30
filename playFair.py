import random
import numpy as np
import math

startingKey = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
cipher = 'AEXVUABZMFWCRPQAFXFPBQGPLXAEVEZDMVUWEVPNFVDOSLEHHPABBVMPDZAESKOVSLIVFBMOPSVFELYZCMZVZVLGCWQWSGDVWYCMZVVFCQFEHIZHVFTBBVAEVFFBMVMPPVBXQWVWIPBXAOQLHTSRAEBVVPPDTMMOMLFWSLEHHPTZAEQATFAIHVKNIDYPDWFZVMMPPIVBIDAEXMGLWFXHMVCQRMXHBVTWFWGCLCPDTMFPBQGPLXSLEHHPWCMOUWSRZVZXMVOFVTAVPSHPTZAEWCATZGEFMFUHVTCBOVCQSRVNPSHPPWCPHPSBPQXHBVFTFBGCIDFTSRIPELCMHTQPSRWQSOWCQOXINPBFVTIGVWMFATZSELNMPMCNPSHPXWAEMVPIPMTMDKHVAISXIPGICZMVVNPSHPPCTEBXSLAGRSIPVPZFWUQAOQIPMPDZAECGGMGDMFWUELEOCWHPIBEXVWSLEHHPWCMOPMOFAEMVLQFBNQZPSLEHHPABGZVFIPZMWQFXMOCQDWGCWCMSPQHTVSWTWUAEVFZVIHOYSLEHHPABLVBHXAFWELVPXHVFMQIPFOKSGPZKLPCWYDMFMPDZAESKIPVXVNPSHPWCNPBFMFAEVFZVHPSNPSHPOFOFMPFTIVMXBVZKLPVZYZDIDBZDVFCQCWVXWQSLEHHPWCRSGMZSXBPCVIBFBXWQMSXMVEZDMIQNPSVFLMHIDSMFIPABWULQVZMPDIKNGPCMVTCRTGFBMOIDAICNPSHPDIDNBXPWOSISMFXNAEMVPQSILVVTZRELLCAEXEWCODGDMFIPIXUWSZGZLQCWSRIGOHVGIGVWVNPSHPBXWCNPBFMFMPUEAEXVWQBFPYFVMOZMPQGCAEWULVWCSZPEISVFBXHPUWGHZGETPHTBGHZIGZMFOVCQGHOCGMZSMXQAZQGLEAULTLSRIPSGAPGZIQZVQPSZGZLQSZCWCMHIETSBCNIPUWIXMPPFZDIPXCWUZSVHQWZNQLFUIPBXSLUEUWIXWCFKGPSRAEMIGZLQSNPSHPWCFPBXSVBXFBUABZMFWCQPYDMFWCEGGPCOCNPSHPABBFHTFBSGWKGIZVPVIGOHCSHVQYPSHPETDNAVPSHPFBAOTVFPBXFTZRGMPMHPSRIPOPCMMIGZMFTFSLEHHPWCQPVOUPPCKATFXMPQGCKWVPMFAEMVLQFBNQZPPIGDMLOQIDAEVFZVBXPQWCMSISMFTFIXVWGCKDPSVOFMPIVOFMWYFTZGUPZDFXFKFBHICNPSHPWCFPBXVWBXHPSNGPOQUABZTFELSOHIKFIPSZPZGZAEVTIGVWVOSBCUDBVNPSHPBXCPOFMPUWSRMPDZAESGGZMFAEXEWCFPBXVNWQHVDZRNBVUEAEXELQFBKTGHGCWYFTIABXNUBFHFTGFVKDXHVEDZBDPYUWSRPCLIPMPCVBPRIPAEVFZVPZPMHPYZTCHTVOLXIDCPFTVDQLFTZSWCQOZPBFMFELCPHXSLEHHPABLVBHBXIHWCMFULTLSVUEAEVFFBMFIPAEOVOVULFBWUSLEDZDAVPSHPBXCPOFMPFTCQIVMXBVMLOQZVIUCQUWHXZVAEHTZFVIBFVOSNVTKWVPMFSLEHHPWCFOXOAQFPZMHTHZVFPDAUTFMPRZWUAQVPMPWVZPSLEHHPTESGAPGZZIGZAEVTIGVWOPDECGXIVNPSHPOVCQGHZHHTGHZQGLEAZSVHSPFBMPPVIPBXSGGZMFELCOXIYPVWGZBXSLAGMSISVFBXEDFBHICUSRBXAEWCFXFPBXHPLUZVWCQPLUZVDIQBOVFBIHPCHVPSHPDIQBMVXHXEMFTCBFSUIZTFHVFBWUWKHVPSHPWCFSBFGUQWFVKTOQIPOEGLEACQIVVPGMPMAEBFHTZAUCVOKVGPCQRSIPSLEXQAZSLYPSHPBXCPOFOPSGAXTCHVBFUWZVGCCPIVMSCGTEMFIPMLPROFSGAXWTTMVWZMXBBFBTHTFBZSGPBRUCPIAEXHXEBFQAQSTFVUPOXHVFBXZKHTPILNPSHPCMHTSVTBFBQSPSHPWCRPMVPIUMTMQPUVGPQNIPUWIXPITWYMVPBXVZLXPFIPABSKGSGPTZCMPIVMMILBHTYDMFMPFTPWVWELEPPOBVMSXMQLFUGDWCCPVNPSHPWCFPBXVNWQHVDZUBPWVWCMOEPITAUWEVRNQWZVVOVWLMOVBXPQSLEHHPCMBFMTZGMFMPUEAEVFZVPZPMHPCWUMTMWQMFPIAEZVQFXHMTGCDIQWSPEXVWMPUEAEBVBXCPOFMPSGPYATDPVMIOSLAGKOTIXEHTBXWQUPXCSLEHHPGLTXYMYMOPSLEHHPMPDZAECUSVTBFBKMMPFTUPGPOQMXPCHTVCPCPILGIVAEMVLQFBNQZPNBTLSVMPUEWFTXSLEHHPAEVFZVPZPMHPZBVFWKVBKMMPPVLSPSHPTESGAPGZAQGHZIPBVFIGIGSCGPDWWQUVSLEHHPZTGZAQOCILIPIPBXXEBFQAQSTFCUSRPCDGIWLMHIDSXH'



quadMap = {}
quadTotal = 0
with open('english_quadgrams.txt') as f:
    quadFreq = f.readlines()
    for quad in quadFreq:
        quadMap[quad[:4]] = int(quad[5:-1])
        quadTotal += int(quad[5:-1])


triMap = {}
triTotal = 0
with open('english_trigrams.txt') as f:
    triFreq = f.readlines()
    for tri in triMap:
        triMap[tri[:3]] = int(tri[4:-1])
        triTotal += int(tri[4:-1])

biMap = {}
biTotal = 0
with open('english_bigrams.txt') as f:
    triFreq = f.readlines()
    for bi in biMap:
        biMap[bi[:3]] = int(bi[4:-1])
        biTotal += int(bi[4:-1])
        

# parameters
temp = 20
s = 1
c = 1000


    
def getQuadProbability(string):
    if string in quadMap:
        return math.log10(quadMap[string])-math.log10(quadTotal)
    else:
        return -9.4
    
def getTriProbability(string):
    if string in triMap:
        return math.log10(triMap[string])-math.log10(triTotal)
    else:
        return -9.4
    
def getBiProbability(string):
    if string in biMap:
        return math.log10(biMap[string])-math.log10(biTotal)
    else:
        return -9.4
    

def testFit(testString):
    totalProbability = 0
    for i in range(len(testString) - 3):
        totalProbability += getQuadProbability(testString[i:i+4])
        
    for i in range(len(testString) - 3):
        totalProbability += getTriProbability(testString[i:i+3])
        
    for i in range(len(testString) - 3):
        totalProbability += getBiProbability(testString[i:i+2])
        
    return totalProbability / 3
        

    
    
def swapRandomElements(key):
    [first, second] = np.sort(random.sample(range(len(key)), 2))
    return key[0:first] + key[second] + key[first + 1: second] + key[first] + key[second + 1:]


def decodePlayfair(key, cipher):
    ret = ""
    for i in range(0, len(cipher), 2):
        x = cipher[i]
        y = cipher[i+1]
        x_index = key.index(x)
        y_index = key.index(y)
        
        x_row = int(x_index / 5)
        x_column = x_index % 5
        
        y_row = int(y_index / 5)
        y_column = y_index % 5
        
        # Go left a column but stay in the same row
        if x_row == y_row:
            if x_column == 0:
                x_result = key[x_index + 4]
                y_result = key[y_index - 1]
            elif y_column == 0:
                x_result = key[x_index - 1]
                y_result = key[y_index + 4]
            else:
                x_result = key[x_index - 1]
                y_result = key[y_index - 1]
                
        # Go up a row but stay in same column
        elif x_column == y_column:
            if x_row == 0:
                x_result = key[x_index + 20]
                y_result = key[y_index - 5]
            elif y_row == 0:
                x_result = key[x_index - 5]
                y_result = key[y_index + 20]
            else:
                x_result = key[x_index - 5]
                y_result = key[y_index - 5]

        else:
            x_result = key[5 * x_row + y_column]
            y_result = key[5 * y_row + x_column]
            
        ret += x_result + y_result
        
    return ret



parentKey = startingKey
parentResult = decodePlayfair(parentKey, cipher)
parentFit = testFit(parentResult)
iteration = 1
while(1):
    print("Iteration: " + str(iteration))
    print("Score: " + str(parentFit))
    print("Key: " + parentKey)
    print(parentResult)
    print("\n")
    t = temp
    while(t >= 0):
        for _ in range(c):
            newKey = swapRandomElements(parentKey)
            newResult = decodePlayfair(newKey, cipher)
            newFit = testFit(newResult)
            
        df = newFit - parentFit
        if df > 0:
            parentKey = newKey
            parentFit = newFit
            parentResult = newResult
        else:
            if t > 0:
                if random.random() < math.e**(df/t):
                    parentKey = newKey
                    parentFit = newFit
                    parentResult = newResult
        t -= s
    iteration += 1