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
    this.getForecast();

  }

  getActualWeather(): any{
    this.client.get<any>('http://localhost:5000/actual-weather',
      { headers: new HttpHeaders({'token': '' + localStorage.getItem('token')})}).subscribe(resp => {
        this.city = resp.city;
        this.temperature = resp.temperature;
        this.actualDate = resp.current_date;
    }, error => {
        alert('Please login before use our services.');
        this.router.navigate(['login']);
    });
  }

  getForecast() {
    this.client.get<Forecast>('http://localhost:5000/forecast',
      { headers: new HttpHeaders({'token': '' + localStorage.getItem('token')})}).subscribe(resp => {
        this.forecastData = resp;
        this.forecastElements = this.forecastData?.list.slice(0, this.actualPage * 10);
    });
  }

  paginateNext() {
    // @ts-ignore
    if(this.forecastData?.list.length / 10 > this.actualPage) {
      this.actualPage++;
      this.forecastElements = this.forecastData?.list.slice((this.actualPage -1) * 10, this.actualPage * 10);
    }
    else {
      alert("This is the end of the list!");
    }
  }

  paginatePrevious() {
    // @ts-ignore
    if(this.actualPage > 1) {
      this.actualPage--;
      this.forecastElements = this.forecastData?.list.slice((this.actualPage -1) * 10, this.actualPage * 10);
    }
    else {
      alert("This is the beginning of the list!");
    }
  }

  logout() {
    localStorage.clear();
    alert('You\'ve successfully logged in.');
    this.router.navigate(['login']);
  }

}
