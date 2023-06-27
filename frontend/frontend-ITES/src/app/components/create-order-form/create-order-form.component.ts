import { Component } from '@angular/core';
import {ProfilePageComponent} from "../../pages/profile-page/profile-page.component";
import {OrdersService} from "../../services/orders.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-create-order-form',
  templateUrl: './create-order-form.component.html',
  styleUrls: ['./create-order-form.component.scss']
})
export class CreateOrderFormComponent {
  constructor(public profilePageComponent: ProfilePageComponent, public ordersService: OrdersService, private router: Router) {
  }

  createOrder(name: string, file: string, description: string) {
    this.ordersService.createOrder(name, file, description)
      .subscribe(res => {
        alert('Заказ создан');
        window.location.reload();
      }, error => {
        alert('Ошибка: ' + error);
      });
  }
}
