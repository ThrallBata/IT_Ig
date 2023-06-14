import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Message} from "../models/message";

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  constructor(private http: HttpClient) { }

  getUserMessageStory(): Observable<Message[]> {
    return this.http.get<Message[]>('http://127.0.0.1:8000/api/chat/', {
      headers: {
        Authorization: 'Token ' + localStorage.getItem('token')
      }
    });
  }
}
