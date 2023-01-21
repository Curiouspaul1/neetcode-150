var isAnagram = function(s, t) {
    sA = s.split('').sort()
    tA = t.split('').sort()

    if(sA.length != tA.length){
        return false
    }
    for(let i=0; i<sA.length; i++)
  
    if(sA[i] != tA[i]){
        return false
    }
    return true
};