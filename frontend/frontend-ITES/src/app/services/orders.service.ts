import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Order} from "../models/order";

@Injectable({
  providedIn: 'root'
})
export class OrdersService {

  constructor(private http: HttpClient) { }

  getAllOrders(): Observable<Order[]> {
    return this.http.get<Order[]>("http://127.0.0.1:8000/api/order/all/", {
      headers: {
        Authorization: "Token " + localStorage.getItem("token")
      }
    });
  }

  getUserOrders(): Observable<Order[]> {
    return this.http.get<Order[]>("http://127.0.0.1:8000/api/order", {
      headers: {
        Authorization: "Token " + localStorage.getItem("token"),
      }
    });
  }

  createOrder(name: string, file: string, description: string) {
    let input = new FormData();
    input.append('file', file);
    return this.http.post("http://127.0.0.1:8000/api/order", {name, input, description},{
      headers: {
        Authorization: "Token " + localStorage.getItem("token")
      }
    });
  }
}
