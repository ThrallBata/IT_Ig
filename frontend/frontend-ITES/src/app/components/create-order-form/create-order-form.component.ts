import { Component } from '@angular/core';
import {ProfilePageComponent} from "../../pages/profile-page/profile-page.component";

@Component({
  selector: 'app-create-order-form',
  templateUrl: './create-order-form.component.html',
  styleUrls: ['./create-order-form.component.scss']
})
export class CreateOrderFormComponent {
  constructor(public profilePageComponent: ProfilePageComponent) {
  }
}
