import streamlit as st
import re

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------
# SAMPLE ORDER DATABASE
# --------------------------------

orders = {
    "FN8183807647": {
        "customer": "Krupa",
        "product": "Smart Watch",
        "status": "Out for Delivery",
        "location": "Hyderabad",
        "delivery": "7 October 2026",
        "updated": "6 October 2026, 11:00 AM"
    },

    "ORD1001": {
        "customer": "Krupa",
        "product": "Wireless Headphones",
        "status": "Shipped",
        "location": "Hyderabad",
        "delivery": "10 October 2026",
        "updated": "6 October 2026, 10:30 AM"
    }
}


# --------------------------------
# CHATBOT FUNCTION
# --------------------------------

def chatbot(message):

    text = message.lower().strip()

    # --------------------------------
    # FIND TRACKING NUMBER
    # --------------------------------

    tracking_id = re.search(
        r"\b[A-Z]{2,4}\d{8,15}\b",
        message.upper()
    )

    # Support ORD1001 format
    if not tracking_id:
        tracking_id = re.search(
            r"\bORD\d{3,15}\b",
            message.upper()
        )

    # --------------------------------
    # TRACKING ID FOUND
    # --------------------------------

    if tracking_id:

        order_id = tracking_id.group().upper()

        if order_id in orders:

            order = orders[order_id]

            return (
                "📦 **Order Tracking**\n\n"
                f"🆔 **Tracking ID:** {order_id}\n\n"
                f"👤 **Customer:** {order['customer']}\n\n"
                f"📦 **Product:** {order['product']}\n\n"
                f"🚚 **Status:** {order['status']}\n\n"
                f"📍 **Current Location:** {order['location']}\n\n"
                f"📅 **Expected Delivery:** {order['delivery']}\n\n"
                f"🕒 **Last Updated:** {order['updated']}"
            )

        else:

            return (
                f"🔍 I found tracking ID **{order_id}**, "
                "but it is not available in our tracking system.\n\n"
                "Please check the tracking number."
            )

    # --------------------------------
    # TRACKING WITHOUT ID
    # --------------------------------

    tracking_words = [
        "track",
        "tracking",
        "where is my order",
        "where is my package",
        "where is my parcel",
        "order status",
        "track my order",
        "track order",
        "my order",
        "package",
        "parcel"
    ]

    if any(word in text for word in tracking_words):

        return (
            "📦 **Order Tracking**\n\n"
            "Sure! Please enter your Order ID or tracking number.\n\n"
            "Example:\n"
            "• `ORD1001`\n"
            "• `FN8183807647`"
        )

    # --------------------------------
    # GREETING
    # --------------------------------

    if any(word in text for word in [
        "hello",
        "hi",
        "hey",
        "hai"
    ]):

        return (
            "👋 **Hello! Welcome to Customer Support.**\n\n"
            "I can help you with:\n\n"
            "📦 Order Tracking\n"
            "💰 Refunds\n"
            "🚚 Delivery\n"
            "🔄 Returns\n"
            "💳 Payments\n"
            "❌ Order Cancellation"
        )

    # --------------------------------
    # REFUND
    # --------------------------------

    if any(word in text for word in [
        "refund",
        "money back",
        "cash back"
    ]):

        return (
            "💰 **Refund Information**\n\n"
            "Refunds are normally processed within "
            "**5-7 business days** after approval."
        )

    # --------------------------------
    # DELIVERY
    # --------------------------------

    if any(word in text for word in [
        "shipping",
        "delivery",
        "deliver"
    ]):

        return (
            "🚚 **Delivery Information**\n\n"
            "Standard delivery usually takes "
            "**3-5 business days**.\n\n"
            "Please provide your tracking number "
            "to check your delivery status."
        )

    # --------------------------------
    # RETURN
    # --------------------------------

    if any(word in text for word in [
        "return",
        "replacement",
        "exchange"
    ]):

        return (
            "🔄 **Return Information**\n\n"
            "You can request a return or replacement "
            "within **7 days** of receiving the product."
        )

    # --------------------------------
    # PAYMENT
    # --------------------------------

    if any(word in text for word in [
        "payment",
        "upi",
        "card"
    ]):

        return (
            "💳 **Payment Information**\n\n"
            "We support:\n"
            "• UPI\n"
            "• Credit Cards\n"
            "• Debit Cards\n"
            "• Net Banking"
        )

    # --------------------------------
    # CANCELLATION
    # --------------------------------

    if any(word in text for word in [
        "cancel order",
        "cancel my order",
        "cancellation"
    ]):

        return (
            "❌ **Order Cancellation**\n\n"
            "Please provide your Order ID to request "
            "order cancellation."
        )

    # --------------------------------
    # THANK YOU
    # --------------------------------

    if "thank" in text:

        return (
            "You're welcome! 😊\n\n"
            "I'm happy to help."
        )

    # --------------------------------
    # DEFAULT RESPONSE
    # --------------------------------

    return (
        "🤖 **I can help you with:**\n\n"
        "📦 Order Tracking\n"
        "💰 Refunds\n"
        "🚚 Delivery\n"
        "🔄 Returns\n"
        "💳 Payments\n"
        "❌ Order Cancellation\n\n"
        "To track an order, enter your tracking number."
    )


# --------------------------------
# STREAMLIT USER INTERFACE
# --------------------------------

st.title("🤖 AI Customer Support Chatbot")

st.write(
    "Welcome! I can help you with order tracking, "
    "refunds, delivery, returns and payments."
)

st.divider()

message = st.text_input(
    "💬 Enter your message",
    placeholder="Example: FN8183807647"
)

if st.button("Send", type="primary"):

    if message.strip():

        response = chatbot(message)

        st.markdown(response)

    else:

        st.warning("⚠️ Please enter a message.")


# --------------------------------
# SAMPLE ORDER IDs
# --------------------------------

st.divider()

st.subheader("📦 Sample Order IDs")

st.code("FN8183807647")
st.code("ORD1001")
