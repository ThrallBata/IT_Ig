import { Component } from '@angular/core';
import {ChatService} from "../../services/chat.service";
import {Message} from "../../models/message";

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent {
  isOpened = false;
  messages: Message[];
  userId: number;
  chatId: number;

  constructor(private chatService: ChatService) {}

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

  /*websocket(userId: number, chatId: number) {
    const roomName = userId;

    const chatSocket = new WebSocket(
      'ws://'
      + window.location.host
      + '/ws/chat/'
      + roomName
      + '/'
    );

    chatSocket.onmessage = function(e) {
      const data = JSON.parse(e.data);
      document.querySelector('#chat-log').value += (data.message + '\n');
    };

    chatSocket.onclose = function(e) {
      console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#chat-message-input').focus();
    document.querySelector('#chat-message-input').onkeyup = function(e) {
      if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
      }
    };

    document.querySelector('#chat-message-submit').onclick = function(e) {
      const messageInputDom = document.querySelector('#chat-message-input');
      const message = messageInputDom.value;
      chatSocket.send(JSON.stringify({
        'message': message,
        'room': roomName,
        'chat': chatId,
      }));
      messageInputDom.value = '';
    };
  }*/
}
