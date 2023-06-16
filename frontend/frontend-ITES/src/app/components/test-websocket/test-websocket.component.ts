import { Component, OnDestroy } from '@angular/core';
import {WebsocketService} from "../../services/websocket.service";


@Component({
  selector: 'app-test-websocket',
  templateUrl: './test-websocket.component.html',
  styleUrls: ['./test-websocket.component.scss']
})
export class TestWebsocketComponent {
  message = '';
  room = '1';
  chat = '1';

  constructor(public webSocketService: WebsocketService) {
    this.webSocketService.connect();
  }

  sendMessage(message: string, room: string, chat: string) {
    this.webSocketService.sendMessage(message, room, chat);
  }

  ngOnDestroy() {
    this.webSocketService.close();
  }
}
