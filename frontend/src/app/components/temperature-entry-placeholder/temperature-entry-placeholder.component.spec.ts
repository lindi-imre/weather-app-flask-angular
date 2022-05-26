import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TemperatureEntryPlaceholderComponent } from './temperature-entry-placeholder.component';

describe('TemperatureEntryPlaceholderComponent', () => {
  let component: TemperatureEntryPlaceholderComponent;
  let fixture: ComponentFixture<TemperatureEntryPlaceholderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TemperatureEntryPlaceholderComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TemperatureEntryPlaceholderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
