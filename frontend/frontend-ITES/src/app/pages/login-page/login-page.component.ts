import {Component} from '@angular/core';
import {NavigationComponent} from "../../components/navigation/navigation.component";
import {Router} from "@angular/router";
import {LoginService} from "../../services/login.service";
import {Observable} from "rxjs";
import {Token} from "../../models/token";

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent {

  constructor(private loginService: LoginService, private router: Router) {
  }

  testLogin(login: string, password: string) {
    this.loginService.testLogin(login, password)
      .subscribe(res => {
        alert('Вход');
        console.log(localStorage.getItem('token'));
        this.router.navigate(['/'])
      }, error => {
        alert('Ошибка');
      });
  }

  /*getUserId() {
    this.loginService.getUserId()
      .subscribe(res => {
        alert("Id пользователя получен");
        console.log(localStorage.getItem('userId'));
      }, error => {
        alert("Ошибка");
      });
  }*/

}
