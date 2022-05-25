import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private client:HttpClient, private router: Router) { }

  ngOnInit(): void {
  }

  doLogin(username: string, password: string) {
    this.client.post<any>('http://localhost:5000/loginjwt', {username: username, password: password}).subscribe(resp =>{
      if(resp.message) {
        alert(resp.message);
      }
      else {
        localStorage.setItem('token', resp.token);
        this.router.navigate(['dashboard']);
      }
    })
  }

}
