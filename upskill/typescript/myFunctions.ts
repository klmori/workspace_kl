// function checkSum(num: number): boolean{
//     if (num > 5){
//         return true
//     }else{
//         return false
//     }
// }


const helloFunction = (s: string): string => {
    return ""
}


const heros = ["thor", "Batman", "Ironman"]

heros.map(hero => {
    return `hero is ${hero}`
})

function errormessage(msg: string): void{
    throw  msg
}




//  Returning Objects

function CrateUser(): {name: string, id: number}{
    return {name: "John", id: 1}
}

type userdata = {
    name: string
    id: number
}

function CrateUser2(data: userdata){
    return {name: "John", id: 1} 
}


// Interface

type User = {
    readonly _id: number
    name: string
    email: string
    isactive: boolean
    atm?: number
}

let userCheck: User = {
    _id: 1,
    name: "krunal",
    email: "i@gmil.com",
    isactive: true,
    // atm: 1333
}

userCheck.atm = 3

// 
let multi: string | number = 33
multi = '33'

type Users = {
    name: string
    id: number
}

type Admin = {
    userName: string
    id: number
}

let checkUs: Users | Admin = {name: "Hoii", id: 1}

const d1: number[] = [1,2,3,4]
const d2: string[] = ["1","2","3"]
const d3: string | number[] = [1,2,3]

let selectBirth: "Upper" | "Lowwer" | "Middle"
selectBirth = "Upper1"


let order: [string, number, boolean]
order = ["1", 1, true]
order = [1, "1", true]

let allowAll: (string | number)[]
allowAll = [1,3,"4"]



// Different Interface and Type  =>  Interface reopen and also extend

