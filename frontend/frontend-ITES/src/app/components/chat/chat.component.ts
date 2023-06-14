import {Component, Injectable} from '@angular/core';
import {ChatService} from "../../services/chat.service";
import {Message} from "../../models/message";
import {WebsocketService} from "../../services/websocket.service";
import {HttpClient} from "@angular/common/http";
import {Subject} from "rxjs";

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})

@Injectable()
export class ChatComponent {
  isOpened = false;
  messages: Message[];
  userId: number;
  chatId: number;

  constructor(
    private chatService: ChatService
  ) {}

  ngOnInit(): void {
    this.getUserMessageStory();
  }

  //это нам надо
  getUserMessageStory() {
    this.chatService.getUserMessageStory()
      .subscribe((messages: Message[]) => {
        this.messages = messages;
        this.chatId = messages[0].chat;
        for (let i = 0; i < messages.length; i++) {
          if (messages[i].user !== 1) {
            this.userId = messages[i].user;
            break;
          }
        }
        console.log(this.userId);
      }, error => {
        alert("Ошибка");
      });
  }


}
