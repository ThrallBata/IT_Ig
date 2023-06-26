import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from "@angular/router";
import {MainPageComponent} from "./pages/main-page/main-page.component";
import {LoginPageComponent} from "./pages/login-page/login-page.component";
import {ProfilePageComponent} from "./pages/profile-page/profile-page.component";
import {ProjectsPageComponent} from "./pages/projects-page/projects-page.component";
import {RegisterPageComponent} from "./pages/register-page/register-page.component";
import {ChatPageComponent} from "./pages/chat-page/chat-page.component";
import {AllChatPageComponent} from "./pages/all-chat-page/all-chat-page.component";

export const routes: Routes = [
  {path: '', component: MainPageComponent},
  {path: 'login', component: LoginPageComponent},
  {path: 'profile', component: ProfilePageComponent},
  {path: 'projects', component: ProjectsPageComponent},
  {path: 'register', component: RegisterPageComponent},
  {path: 'chat', component: ChatPageComponent},
  {path: 'chatList', component: AllChatPageComponent}
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
