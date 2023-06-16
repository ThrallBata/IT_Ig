/*import { Injectable } from '@angular/core';
import * as Rx from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class WebsocketService {

  constructor() {}
  private subject: Rx.Subject<MessageEvent>;
  public connect(url: string): Rx.Subject<MessageEvent> {
    if (!this.subject) {
      this.subject = this.create(url);
      console.log("Successfully connected: " + url);
    }
    return this.subject;
  }
  private create(url: string | URL): Rx.Subject<MessageEvent> {
    let ws = new WebSocket(url);
    let observable = Rx.Observable.create((obs: Rx.Observer<MessageEvent>) => {
      ws.onmessage = obs.next.bind(obs);
      ws.onerror = obs.error.bind(obs);
      ws.onclose = obs.complete.bind(obs);
      return ws.close.bind(ws);
    });
    let observer = {
      next: (data: Object) => {
        if (ws.readyState === WebSocket.OPEN) {
          ws.send(JSON.stringify(data));
        }
      }
    };
    return Rx.Subject.create(observer, observable);
  }
}*/

import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

interface MessageData {
  message: string;
  room: string;
  chat: string;
}

@Injectable({
  providedIn: 'root',
})
export class WebsocketService {

  private socket$!: WebSocketSubject<any>;
  public receivedData: MessageData[] = [];

  public connect(): void {
    if (!this.socket$ || this.socket$.closed) {
      this.socket$ = webSocket("ws://localhost:8000/ws/chat/1/");

      this.socket$.subscribe((data: MessageData) => {
        this.receivedData.push(data);
      });
    }
  }

  sendMessage(message: string, room: string, chat: string) {
    this.socket$.next({ message, room, chat });
  }

  close() {
    this.socket$.complete();
  }

}
