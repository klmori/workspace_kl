import { Body, Controller, Get ,HttpCode,Param,Post} from '@nestjs/common';

@Controller('property')
export class PropertyController {
    @Get()
    findall(){
        return "All Products"
    }
    // @Get(":id")
    // getData(@Param("id") id: string){
    //     return id
    // }

    @Get(":id/:data")
    getAllId(@Param()id){
        return id
    }

    @Post()
    @HttpCode(202)
    Create(@Body()body){
        return body
    }
}
