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

  login(credentials) {
    return this.http.post(`${environment.API_URL}/auth/login`, credentials, environment.API_HEADERS);
  }

  logout() {
    return this.http.delete(`${environment.API_URL}/auth/logout`, environment.API_HEADERS);
  }

  async isLogged(){
    let user : any
    if(this.getUserId()){
      await this.getOne(this.getUserId()).toPromise().then(resp => {user = resp}, msg => {user = false});
      if(user){
        return true
      }
    }
    return false
  }

  async isAdmin(){ 
    let roles : any
    let isAdmin = false;
    if(this.getUserId()){
      await this.getRoles(this.getUserId()).toPromise().then(resp => {roles = resp}, msg => {roles = false});
      if(roles){
        Object(roles).forEach((role) => {
          if(role["name"] == "admin"){
            isAdmin = true
          }
        })
      }
    }
    return isAdmin
  }

  getDecodedToken(token) {
    try{
      return jwt_decode(token);
    }
    catch(Error){
      return null;
    }
  }
  
  getUserId() {
    let token = this.getDecodedToken(this.cookie.get("token"))
    if(token){
      return token['user']['id']
    }
    return false
  }
}
