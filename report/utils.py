import os
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from trip.models import Trip

def generate_trip_report(trip):
    """Generate a PDF report for a trip and return its URL"""
    pdf_filename = f"trip_{trip.id}_report.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, "reports", pdf_filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    # Create PDF
    c = canvas.Canvas(pdf_path, pagesize=A4)

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(200, 800, "Trip Report")

    c.setFont("Helvetica", 12)
    
    # Trip Details
    c.drawString(100, 770, f"Driver: {trip.user.username}")
    c.drawString(100, 750, f"Start Location: {trip.start_location}")
    c.drawString(100, 730, f"End Location: {trip.end_location}")
    c.drawString(100, 710, f"Start Date: {trip.start_date.strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 690, f"End Date: {trip.end_date.strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100, 670, f"Total Distance: {trip.totalDistance} Mils")
    c.drawString(100, 650, f"Total Duration: {trip.totalDuration} hours")
    c.drawString(100, 630, f"Required Breaks: {trip.requiredBreaks}")
    c.drawString(100, 610, f"Required Rests: {trip.requiredRests}")

    c.save()

    # Store the report URL in the model
    report_url = os.path.join(settings.MEDIA_URL, "reports", pdf_filename)
    trip.report_url = report_url
    trip.save(update_fields=["report_url"])

    return report_url
