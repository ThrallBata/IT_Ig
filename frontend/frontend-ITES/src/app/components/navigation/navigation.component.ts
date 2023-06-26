import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {LoginService} from "../../services/login.service";
import {AppComponent} from "../../app.component";

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent {

  constructor(private router: Router, public loginService: LoginService, public appComponent: AppComponent) {
  }

  isMenuOpened = false;

  loginBtn() {
    this.router.navigate(['login']);
  }

  profileBtn() {
    this.router.navigate(['profile']);
  }

  registerBtn() {
    this.router.navigate(['register']);
  }

  isAuthorized(): boolean {
    return this.loginService.isAuthorized();
  }

  logout() {
    return this.loginService.logout();
  }

}
