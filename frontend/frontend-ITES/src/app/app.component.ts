import {Component, OnInit} from '@angular/core';
import {LoginService} from "./services/login.service";
import {ProjectsService} from "./services/projects.service";
import {Router} from "@angular/router";
import {ChatComponent} from "./components/chat/chat.component";
import {ChatService} from "./services/chat.service";
import {Message} from "./models/message";
import {UserId} from "./models/userId";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  isAdmin: boolean;
  userId: string;

  constructor(
    private router: Router,
    private chatService: ChatService,
    public loginService: LoginService
  ) {
  }

  getUserId() {
    this.loginService.getUserId()
      .subscribe((userId: UserId) => {
        this.userId = userId.user_id.toString();
        localStorage.setItem("userId", this.userId);
        console.log(localStorage.getItem("userId"));
        this.isAdmin = localStorage.getItem("userId") === "1";
      });
  }

  ngOnInit(): void {

  }
}
