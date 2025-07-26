from pathlib import Path

markdown_content = """
# 🧾 NestJS Validation, DTOs & Pipes – All-in-One Guide

---

## 📦 1. DTO (Data Transfer Object)

A DTO defines the **shape** and **rules** for incoming request data.

```ts
// create-user.dto.ts
import { IsString, IsEmail, IsOptional, Length } from 'class-validator';

export class CreateUserDto {
  @IsString()
  @Length(2, 20)
  name: string;

  @IsEmail()
  email: string;

  @IsOptional()
  @IsString()
  bio?: string;
}



// main.ts
import { ValidationPipe } from '@nestjs/common';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  // Enable global validation
  app.useGlobalPipes(new ValidationPipe({
    whitelist: true,         // Strip unallowed properties
    forbidNonWhitelisted: true, // Throw error on extra props
    transform: true          // Transform payloads to DTO class instances
  }));

  await app.listen(3000);
}



import { Body, Controller, Get, Param, Post, Query, ParseIntPipe } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';

@Controller('users')
export class UsersController {
  
  // POST /users
  @Post()
  createUser(@Body() createUserDto: CreateUserDto) {
    return { message: 'User created', data: createUserDto };
  }

  // GET /users/:id
  @Get(':id')
  getUser(@Param('id', ParseIntPipe) id: number) {
    return `User ID is ${id}`;
  }

  // GET /users?page=2
  @Get()
  getUsers(@Query('page', ParseIntPipe) page: number) {
    return `Getting users from page ${page}`;
  }
}


| Pipe               | Purpose                         |
| ------------------ | ------------------------------- |
| `ParseIntPipe`     | Convert string to number        |
| `ParseBoolPipe`    | Convert string to boolean       |
| `ParseUUIDPipe`    | Validate UUID format            |
| `DefaultValuePipe` | Provide default if undefined    |
| `ValidationPipe`   | Enable validation and transform |


| Decorator           | Description                        |
| ------------------- | ---------------------------------- |
| `@IsString()`       | Must be a string                   |
| `@IsEmail()`        | Must be a valid email              |
| `@IsInt()`          | Must be an integer                 |
| `@IsOptional()`     | Property is optional               |
| `@Length(min, max)` | Must be within string length range |
| `@IsUUID()`         | Must be a valid UUID               |
| `@IsBoolean()`      | Must be true/false                 |



// users.controller.ts
import { Controller, Post, Get, Param, Body, Query, ParseIntPipe } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';

@Controller('users')
export class UsersController {
  
  @Post()
  create(@Body() dto: CreateUserDto) {
    return { success: true, data: dto };
  }

  @Get(':id')
  getOne(@Param('id', ParseIntPipe) id: number) {
    return { userId: id };
  }

  @Get()
  filter(@Query('page', ParseIntPipe) page: number) {
    return { page };
  }
}
