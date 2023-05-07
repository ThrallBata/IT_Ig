import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { MainPageComponent } from './pages/main-page/main-page.component';
import { LoginPageComponent } from './pages/login-page/login-page.component';
import { ProjectsPageComponent } from './pages/projects-page/projects-page.component';
import { ProfilePageComponent } from './pages/profile-page/profile-page.component';
import { NavigationComponent } from './components/navigation/navigation.component';
import { ChatComponent } from './components/chat/chat.component';
import { LoginFormComponent } from './components/login-form/login-form.component';
import { ProjectItemComponent } from './components/project-item/project-item.component';
import { OrderItemComponent } from './components/order-item/order-item.component';
import { RegisterPageComponent } from './pages/register-page/register-page.component';
import { ChatPageComponent } from './pages/chat-page/chat-page.component';

@NgModule({
  declarations: [
    AppComponent,
    MainPageComponent,
    LoginPageComponent,
    ProjectsPageComponent,
    ProfilePageComponent,
    NavigationComponent,
    ChatComponent,
    LoginFormComponent,
    ProjectItemComponent,
    OrderItemComponent,
    RegisterPageComponent,
    ChatPageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
