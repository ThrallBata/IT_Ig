import { Injectable } from '@angular/core';
import {Router} from "@angular/router";
import {HttpClient} from "@angular/common/http";
import {Token} from "../models/token";
import {Observable, tap} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  isAuth = false;

  constructor(private router: Router, private http: HttpClient) {}

  //это чисто фронтовая тема
  login() {
    this.isAuth = true;
    this.router.navigate(['']);
  }

  //это нам надо
  testLogin(login: string, password: string): Observable<Token> {
    return this.http.post<Token>('http://127.0.0.1:8000/auth/token/login/',
      {
        username: login,
        password: password
      }).pipe(
        tap(token => {
          localStorage.setItem('token', token.auth_token)
        })
    )
  }

  //это нам надо
  isAuthorized(): boolean {
    return !!localStorage.getItem('token');
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigate(['/'])
    return this.http.get('http://127.0.0.1:8000/auth/token/logout/');
  }

  //это нам надо
  getUserId() {
    return this.http.get('http://127.0.0.1:8000/api/userid', {
      headers: {
        Authorization: 'Token ' + localStorage.getItem('token')
      }
    })
  }

  //это чисто фронтовая тема
  testLogout() {
    this.isAuth = false;
    this.router.navigate(['login']);
  }
}
