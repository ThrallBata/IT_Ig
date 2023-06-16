import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Message} from "../models/message";

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  messages: Message[];
  userId: string;
  chatId: string;

  constructor(
    private http: HttpClient
  ) {}

  getUserMessageStory(): Observable<Message[]> {
    return this.http.get<Message[]>('http://127.0.0.1:8000/api/chat/', {
      headers: {
        Authorization: 'Token ' + localStorage.getItem('token')
      }
    });
  }

  getChatId(): string {
    this.getUserMessageStory()
      .subscribe((messages: Message[]) => {
        this.messages = messages;
        this.chatId = messages[0].chat;
      }, error => {
        alert("Ошибка");
      });
    return this.chatId;
  }

  getUserId(): string {
    this.getUserMessageStory()
      .subscribe((messages: Message[]) => {
        this.messages = messages;
        for (let i = 0; i < messages.length; i++) {
          if (messages[i].user !== 1) {
            this.userId = messages[i].user.toString();
            break;
          }
        }
      }, error => {
        alert("Ошибка");
      });
    return this.userId;
  }
}
