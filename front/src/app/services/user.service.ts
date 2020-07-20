import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../../environments/environment';
import * as jwt_decode from "jwt-decode";
import { CookieService } from 'ngx-cookie-service';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient, private cookie: CookieService) { }

  getOne(id: string) {
    return this.http.get(`${environment.API_URL}/users/${id}`, environment.API_HEADERS);
  }

  getRoles(id: string) {
    return this.http.get(`${environment.API_URL}/users/${id}/roles`, environment.API_HEADERS);
  }
  
  getUserId() {
    let payload = jwt_decode(this.cookie.get("token"))
    return payload['user']['id']
  }
}
