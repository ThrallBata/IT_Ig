import {Component, Input} from '@angular/core';
import {Chat} from "../../models/chat";
import {ChatService} from "../../services/chat.service";
import {WebsocketService} from "../../services/websocket.service";
import {Router} from "@angular/router";
import {AllChatPageComponent} from "../../pages/all-chat-page/all-chat-page.component";

@Component({
  selector: 'app-chat-item',
  templateUrl: './chat-item.component.html',
  styleUrls: ['./chat-item.component.scss']
})
export class ChatItemComponent {
  @Input() chat: Chat;

  constructor(public chatService: ChatService,
              private webSocketService: WebsocketService,
              private router: Router,
              private allChatPageComponent: AllChatPageComponent) {
  }

  connectToChat(chatId: string): void {
    this.chatService.connectToChatByEmployee(chatId);
    this.allChatPageComponent.getEmployeeMessageStory(chatId);
    this.webSocketService.connect(chatId);
    this.router.navigate(["chat"]);
  }
}
