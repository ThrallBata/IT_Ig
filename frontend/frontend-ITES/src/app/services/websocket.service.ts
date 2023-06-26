import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

interface MessageData {
  message: string;
  chat: string;
  user: string;
}

@Injectable({
  providedIn: 'root',
})
export class WebsocketService {

  private socket$!: WebSocketSubject<any>;
  public receivedData: MessageData[] = [];

  public connect(chatId: string): void {
    if (!this.socket$ || this.socket$.closed) {
      this.socket$ = webSocket("ws://localhost:8000/ws/chat/" + chatId + "/");
      this.socket$.subscribe((data: MessageData) => {
        this.receivedData.push(data);
      });
    }
  }

  sendMessage(message: string, chat: string, user: string) {
    this.socket$.next({ message, chat, user });
  }

  close() {
    this.socket$.complete();
  }

}
