import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Message} from "../models/message";
import {Chat} from "../models/chat";

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

  getUserMessageStory(): Observable<Message[]> | Observable<Chat[]> | any {
    try {
      return this.http.get<Message[]>('http://127.0.0.1:8000/api/chat/', {
        headers: {
          Authorization: 'Token ' + localStorage.getItem('token')
        }
      });
    } catch (error) {
      if (error instanceof TypeError) {
        return this.http.get<Chat[]>('http://127.0.0.1:8000/api/chat/', {
          headers: {
            Authorization: 'Token ' + localStorage.getItem('token')
          }
        });
      } else {
        alert("Ошибка");
      }
    }
  }

  getChatId(): string {
    this.getUserMessageStory()
      .subscribe((messages: Message[]) => {
        this.messages = messages;
        this.chatId = messages[0].chat;
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
          } else {
            this.userId = messages[i].user.toString();
            console.log(this.userId);
          }
        }
      });
    return this.userId;
  }
}
