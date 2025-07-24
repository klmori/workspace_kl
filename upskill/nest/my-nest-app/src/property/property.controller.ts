import { Controller, Get ,Post} from '@nestjs/common';

@Controller('property')
export class PropertyController {
    @Get()
    findall(){
        return "All Products"
    }

    @Post()
    Create(){
        return "This will create all property"
    }
}
