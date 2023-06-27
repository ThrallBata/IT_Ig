import {Component, OnInit} from '@angular/core';
import {CreateOrderFormComponent} from "../../components/create-order-form/create-order-form.component";
import {OrdersService} from "../../services/orders.service";
import {Order} from "../../models/order";

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.scss']
})
export class ProfilePageComponent implements OnInit{
  isCreateOrderFormOpened = false;
  orders: Order[];

  constructor(private ordersService: OrdersService) {
  }

  getUserOrders() {
    this.ordersService.getUserOrders()
      .subscribe((orders: Order[]) => {
        this.orders = orders;
      });
  }

  ngOnInit(): void {
    this.getUserOrders();
  }


}
