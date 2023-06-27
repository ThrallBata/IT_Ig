import {Component, Input} from '@angular/core';
import {Order} from "../../models/order";

@Component({
  selector: 'app-order-item',
  templateUrl: './order-item.component.html',
  styleUrls: ['./order-item.component.scss']
})
export class OrderItemComponent {
  @Input() order: Order;

  details = false;
}
