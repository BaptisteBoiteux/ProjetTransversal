import { Injectable } from '@angular/core';
import { Observable, Timestamp } from 'rxjs';
import { HttpClient } from '@angular/common/http';

const baseUrl = "http://localhost:8080/api"

@Injectable({
  providedIn: 'root'
})
export class Bdd2WebService {

  constructor(private http: HttpClient) { }

  getAllRde() : Observable<any> {
    return this.http.get(baseUrl+"/rondes")
  }

  getAllUsr() : Observable<any> {
    return this.http.get(baseUrl+"/users")
  }

  postUsr(data :{login:string, password:string}) : Observable<any> {
    return this.http.post(baseUrl+"/user", data)
  }
}