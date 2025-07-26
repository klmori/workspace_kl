import { IsInt, IsPort, IsPositive, IsString, Length } from "class-validator"
import { group } from "console"


export class createValidatorsDto{
    @IsString({always: true})
    @Length(2,5,{message: "Error on length"})
    name: string 
    @IsString({always: true})
    @Length(2, 5, { groups: ['create'] })
    @Length(2, 10, { groups: ['update'] })
    desc: string 
    @IsInt()
    @IsPositive()
    area: Number
}