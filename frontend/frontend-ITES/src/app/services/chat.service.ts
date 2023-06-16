import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable, Subject} from "rxjs";
import {Message} from "../models/message";
import {WebsocketService} from "./websocket.service";
import { webSocket } from "rxjs/webSocket";

export interface MessageI {
  author: string;
  message: string;
}

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  public messagesI: any;
  // web: any;

  constructor(
    private http: HttpClient
  ) {
    /*this.web = wsService.connect("ws://localhost:8000/ws/chat/1/");
    this.web.send(JSON.stringify("data"));*/
    /*.map(
      (response: MessageEvent): MessageI => {
        return JSON.parse(response.data)
      }
    )*/
  }

  getUserMessageStory(): Observable<Message[]> {
    return this.http.get<Message[]>('http://127.0.0.1:8000/api/chat/', {
      headers: {
        Authorization: 'Token ' + localStorage.getItem('token')
      }
    });
  }
}
