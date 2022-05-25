import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Router} from "@angular/router";
import {Forecast, ForecastElement} from "../../models/forecast.model";

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private client: HttpClient, private router: Router) { }

  actualPage: number = 1;
  city: string = '';
  temperature: number = 0;
  actualDate: string = '';
  forecastData: Forecast | undefined;
  forecastElements: ForecastElement[] | undefined;

  ngOnInit(): void {
    this.getActualWeather();
  }

  getActualWeather(): any{
    this.client.get<any>('http://localhost:5000/actual-weather',
      { headers: new HttpHeaders({'token': '' + localStorage.getItem('token')})}).subscribe(resp => {
        this.city = resp.city;
        this.temperature = resp.temperature;
        this.actualDate = resp.current_date;
        console.log(resp);
    }, error => {
        alert('Please login before use our services.');
        this.router.navigate(['login']);
    });
  }

}
