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

  getAll() {
    return this.http.get(`${environment.API_URL}/users`, environment.API_HEADERS);
  }

  getRoles(id: string) {
    return this.http.get(`${environment.API_URL}/users/${id}/roles`, environment.API_HEADERS);
  }

  getDecodedToken(token) {
    try{
      return jwt_decode(token);
    }
    catch(Error){
      return null;
    }
  }

  login(credentials) {
    return this.http.post(`${environment.API_URL}/auth/login`, credentials, environment.API_HEADERS);
  }

  isLogged(){
    return this.getDecodedToken(this.cookie.get("token"))
  }
  
  getUserId() {
    let token = this.getDecodedToken(this.cookie.get("token"))
    if(token){
      return token['user']['id']
    }
    return false
  }
}
