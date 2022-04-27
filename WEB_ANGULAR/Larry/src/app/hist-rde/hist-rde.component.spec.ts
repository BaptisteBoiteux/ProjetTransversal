import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistRdeComponent } from './hist-rde.component';

describe('HistRdeComponent', () => {
  let component: HistRdeComponent;
  let fixture: ComponentFixture<HistRdeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HistRdeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HistRdeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
