import { Component } from '@angular/core';
import {Router} from "@angular/router";
import {LoginService} from "../../services/login.service";

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.scss']
})
export class NavigationComponent {

  constructor(private router: Router, public loginService: LoginService) {
  }

  isMenuOpened = false;

  loginBtn() {
    this.router.navigate(['login']);
  }

  profileBtn() {
    this.router.navigate(['profile']);
    // при вызове функции getUserId в ответ приходит ошибка 404 not found
    this.loginService.getUserId()
      .subscribe(res => {
        alert("Id пользователя получен");
        console.log(localStorage.getItem('userId'));
      }, error => {
        alert("Ошибка");
      });
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
