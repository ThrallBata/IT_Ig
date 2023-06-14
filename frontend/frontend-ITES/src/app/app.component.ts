import {Component, OnInit} from '@angular/core';
import {LoginService} from "./services/login.service";
import {ProjectsService} from "./services/projects.service";
import {Router} from "@angular/router";
import {ChatComponent} from "./components/chat/chat.component";
import {ChatService} from "./services/chat.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {

  notifications: any = [];

  constructor(
    private router: Router,
    private chatService: ChatService
  ) {
    /*chatService.messagesI.subscribe((msg: { message: any; }) => {
      this.notifications.unshift(msg.message);
    });*/
  }

}
