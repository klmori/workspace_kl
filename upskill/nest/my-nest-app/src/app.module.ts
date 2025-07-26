import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PropertyModule } from './property/property.module';
import { ValidatorsModule } from './validators/validators.module';

@Module({
  imports: [PropertyModule, ValidatorsModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
