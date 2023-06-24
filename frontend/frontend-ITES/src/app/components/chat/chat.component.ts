import {Component, Injectable} from '@angular/core';
import {ChatService} from "../../services/chat.service";
import {Message} from "../../models/message";
import {WebsocketService} from "../../services/websocket.service";

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})

@Injectable()
export class ChatComponent {
  isOpened = false;
  messages: Message[];
  message = '';

  constructor(
    public chatService: ChatService,
    public webSocketService: WebsocketService
  ) {}

  ngOnInit(): void {
    this.getUserMessageStory();
    this.chatService.getChatId();
    this.chatService.getUserId();
    this.webSocketService.connect(this.chatService.chatId);
  }

  //это нам надо
  getUserMessageStory() {
    this.chatService.getUserMessageStory()
      .subscribe((messages: Message[]) => {
        this.messages = messages;
      });
  }

  sendMessage(message: string, chat: string, userId: string) {
    this.webSocketService.sendMessage(message, chat, userId);
  }

  ngOnDestroy() {
    this.webSocketService.close();
  }
}
