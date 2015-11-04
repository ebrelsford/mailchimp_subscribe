mailchimp_subscribe
===================

A very simple python module for subscribing users to a Mailchimp mailing list.


Installation
------------

Use pip.


Usage
-----

Proved the ``API_KEY``, ``LIST_ID``, and ``EMAIL_ADDRESS``::

    from mailchimp_subscribe import subscribe

    subscribe(<API_KEY>, <LIST_ID>, <EMAIL_ADDRESS>)
