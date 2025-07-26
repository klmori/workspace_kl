import { Body, Controller, Get, Param, ParseBoolPipe, ParseIntPipe, Post, Query, UsePipes, ValidationPipe} from "@nestjs/common";
import { createValidatorsDto } from './dto/createvalidators.dto';

@Controller('validators')
export class ValidatorsController {
    @Get(':id')
    greetings(@Param('id',ParseIntPipe)id, @Query('sort',ParseBoolPipe) sort){
        return sort
    }

    // @Post()
    // @UsePipes(new ValidationPipe({whitelist: true, forbidNonWhitelisted: true}))
    // getDto(@Body() body: createValidatorsDto){
    //     return body
    // }

    @Post()
    // @UsePipes(new ValidationPipe({whitelist: true, forbidNonWhitelisted: true}))
    getDto(@Body(new ValidationPipe({whitelist: true, forbidNonWhitelisted: true})) body: createValidatorsDto){
        return body
    }

    @Post("/create")
    create(
        @Body(
            new ValidationPipe({
                whitelist: true,
                forbidNonWhitelisted: true,
                groups: ['create'],
            })
        )body: createValidatorsDto,
    ){
        return body
    }
    @Post("/update")
    update(
        @Body(
            new ValidationPipe({
                whitelist: true,
                forbidNonWhitelisted: true,
                groups: ['update'],
                always: true
            })
        )body: createValidatorsDto,
    ){
        return body
    }
}