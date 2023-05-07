import { Component } from '@angular/core';
import {NavigationComponent} from "../../components/navigation/navigation.component";
import {Router} from "@angular/router";
import {LoginService} from "../../services/login.service";

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent {

  constructor(public loginService: LoginService) {
  }

}
