import { Module } from '@nestjs/common';
import { ValidatorsController } from './validators.controller';

@Module({
    controllers: [ValidatorsController]
})
export class ValidatorsModule {}
