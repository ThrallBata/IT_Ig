import { Injectable } from '@angular/core';
import {Router} from "@angular/router";

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  isAuth = false;

  constructor(private router: Router) {}

  login() {
    this.isAuth = true;
    this.router.navigate(['']);
  }

  logout() {
    this.isAuth = false;
    this.router.navigate(['login']);
  }
}
