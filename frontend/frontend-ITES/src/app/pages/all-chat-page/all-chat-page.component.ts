import {Component, OnInit} from '@angular/core';
import {Chat} from "../../models/chat";
import {ChatService} from "../../services/chat.service";
import {WebsocketService} from "../../services/websocket.service";
import {Router} from "@angular/router";
import {Observable} from "rxjs";
import {Message} from "../../models/message";
import {ChatComponent} from "../../components/chat/chat.component";

@Component({
  selector: 'app-all-chat-page',
  templateUrl: './all-chat-page.component.html',
  styleUrls: ['./all-chat-page.component.scss']
})
export class AllChatPageComponent implements OnInit{
  chats: Chat[];

  constructor(private chatService: ChatService) {
  }

  ngOnInit(): void {
    this.getChatList();
  }

  getChatList() {
    this.chatService.getUserMessageStory()
      .subscribe((chats: Chat[]) => {
        this.chats = chats;
      });
  }

  getEmployeeMessageStory(chatId: string) {
    this.chatService.connectToChatByEmployee(chatId)
      .subscribe((messages: Message[]) => {
      this.chatService.messages = messages;
    });
  }
}
