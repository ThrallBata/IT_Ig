import { Component } from '@angular/core';
import {CreateOrderFormComponent} from "../../components/create-order-form/create-order-form.component";

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.scss']
})
export class ProfilePageComponent {
  isCreateOrderFormOpened = false;
}
