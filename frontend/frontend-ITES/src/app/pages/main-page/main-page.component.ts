import { Component } from '@angular/core';
import {LoginService} from "../../services/login.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss']
})
export class MainPageComponent {
  constructor(private loginService: LoginService, private router: Router) {
  }

  redirect() {
    if (this.loginService.isAuthorized()) {
      this.router.navigate(['chat']);
    } else {
      this.router.navigate(['login']);
    }
  }
}
