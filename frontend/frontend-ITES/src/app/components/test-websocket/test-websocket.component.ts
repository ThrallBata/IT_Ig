import { ChangeDetectionStrategy, Component, OnDestroy, OnInit, ViewEncapsulation, AfterViewInit } from '@angular/core';
import { map, tap, catchError, retry } from 'rxjs/operators';
import {WebsocketService} from "../../services/websocket.service";

@Component({
  selector: 'app-test-websocket',
  templateUrl: './test-websocket.component.html',
  styleUrls: ['./test-websocket.component.scss'],
  encapsulation: ViewEncapsulation.None,
  changeDetection: ChangeDetectionStrategy.OnPush
})
export class TestWebsocketComponent implements AfterViewInit {

  transactions$ = this.service.messages$.pipe(
    map(rows => rows['data']),
    catchError(error => { throw error }),
    tap({
      error: error => console.log('[Live Table component] Error:', error),
      complete: () => console.log('[Live Table component] Connection Closed')
    })
  );

  constructor(private service: WebsocketService) {
  }

  ngAfterViewInit() {
    this.service.connect();
  }
}
