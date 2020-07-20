import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from './../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class MeetupService {

  constructor(private http: HttpClient) { }

  getOne(id: string) {
    return this.http.get(`${environment.API_URL}/meetups/${id}`, environment.API_HEADERS);
  }

  getUsers(id: string) {
    return this.http.get(`${environment.API_URL}/meetups/${id}/users`, environment.API_HEADERS);
  }

  getBeers(id: string) {
    return this.http.get(`${environment.API_URL}/meetups/${id}/beers`, environment.API_HEADERS);
  }

  getTemperature(id: string) {
    return this.http.get(`${environment.API_URL}/meetups/${id}/temperature`, environment.API_HEADERS);
  }
}
