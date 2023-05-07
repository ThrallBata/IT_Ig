import { Injectable } from '@angular/core';
import {Router} from "@angular/router";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  isAuth = false;

  constructor(private router: Router, private http: HttpClient) {}

  login() {
    this.isAuth = true;
    this.router.navigate(['']);
  }

  testLogin(login: string, password: string) {

    return this.http.post('http://127.0.0.1:8000/auth/token/login/',
      {
        username: login,
        password: password
      }).subscribe(res => {
      alert("Вход");
    }, error => {
      alert("Ошибка");
    });
  }

  logout() {
    this.isAuth = false;
    this.router.navigate(['login']);
  }
}
