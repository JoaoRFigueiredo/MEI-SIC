// reservations.component.ts
import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
import { Calendar } from '@fullcalendar/core';
import timeGridPlugin from '@fullcalendar/timegrid';
import dayGridPlugin from '@fullcalendar/daygrid';
import { AppointmentService } from '../_services/appointment.service';
import { AuthService } from '../_services/auth.service';
import { MatDialog } from '@angular/material/dialog';

@Component({
  selector: 'app-reservations',
  templateUrl: './reservations.component.html',
  styleUrls: ['./reservations.component.css']
})
export class ReservationsComponent implements AfterViewInit {
  @ViewChild('calendar') calendarRef!: ElementRef;
  calendar: any;
  appointments: any[] = [];
  selectedAppointment: any; // Variável para rastrear o compromisso selecionado
  userEmail: string | null;

  constructor(private userService: AuthService, private appointmentService: AppointmentService, private dialog: MatDialog) {
    this.userEmail = this.userService.getUserEmail();
  }
  ngAfterViewInit() {
    this.appointmentService.getAppointmentsFromPlace('Solario 1').subscribe(appointments => {
      this.appointments = appointments;
      console.log("this.appointments -> " + this.appointments)
      this.initCalendar();
    });
  }

  initCalendar() {
    const filteredAppointments = this.appointments.filter(appointment => {
      if (this.userEmail != null) {
        return appointment.accountable.trim() != null;
      } else {
        return null;
      }
    });

    this.calendar = new Calendar(this.calendarRef.nativeElement, {
      plugins: [dayGridPlugin, timeGridPlugin],
      initialView: 'timeGridWeek',
      slotDuration: '00:30:00',
      views: {
        timeGrid: {
          allDaySlot: false, // Remova a visualização All Day
          slotHeight: 300, // Ajuste a altura conforme necessário
        },
      },
      slotMinTime: '08:00:00',
      slotMaxTime: '22:00:00',
      slotLabelContent: (arg) => {
        const date = arg.date;
        const formattedTime = date.toLocaleTimeString('en-US', {
          hour: '2-digit',
          minute: '2-digit',
          hour12: false,
        });
        return formattedTime;
      },
      contentHeight: 'auto',
      events: filteredAppointments.map(appointment => {
        const eventDate = new Date(appointment.day);
        const eventEndDate = new Date(appointment.day);
        eventEndDate.setMinutes(eventEndDate.getMinutes() + 30);

        const formattedTime = eventDate.toLocaleTimeString('pt-BR', {
          hour: '2-digit',
          minute: '2-digit',
        });
        const formattedEndTime = eventEndDate.toLocaleTimeString('pt-BR', {
          hour: '2-digit',
          minute: '2-digit',
        });

        const title = ` ${appointment.name}`;

        return {
          title: title,
          start: eventDate,
          end: eventEndDate,
          classNames: ['fc-event-time'],
          appointmentDetails: appointment,
        };
      }),

      eventClick: (info) => {
        this.selectedAppointment = info.event.extendedProps.appointmentDetails;
        this.openDetailsModal(this.selectedAppointment);
      }
    });

    this.calendar.render();
  }
  openDetailsModal(appointment: any): void {
    // Define os detalhes do compromisso selecionado
    this.selectedAppointment = appointment;
  }

  formatDateAndTime(dateTime: string): string {
    const formattedDateTime = new Date(dateTime);
    
    // Definir opções de formato para data
    const dateOptions: Intl.DateTimeFormatOptions = {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
    };
  
    // Obter a parte da data no formato desejado
    const formattedDate = formattedDateTime.toLocaleDateString('pt-PT', dateOptions);
  
    // Definir opções de formato para hora
    const timeOptions: Intl.DateTimeFormatOptions = {
      hour: '2-digit',
      minute: '2-digit',
    };
  
    // Obter a parte da hora no formato desejado
    const formattedTime = formattedDateTime.toLocaleTimeString('pt-PT', timeOptions);
  
    // Retornar a data e hora formatadas
    return `${formattedDate}, ${formattedTime}`;
  }
  


}
