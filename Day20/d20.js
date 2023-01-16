// create a variable l,r = 0, 1
// while r < s.length:
// check if s[l] + s[r] = "()" or "{}" or "[]"
// left ++
// right ++
// continue
// else return False
// return True

const isValid = (s) =>{
    let stack = []
    let closeToOpen = {
    "}" :"{",
    ")" : "(",
    "]" : "[" 
    }
   // for (let i in s)()
   for (let i in Object.values(closeToOpen)) {console.log(i)}
}

let s = "()[]{}"
console.log(isValid(s))

