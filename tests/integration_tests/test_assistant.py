import logging
import logging.config

import zai
from zai import ZaiClient


def test_assistant(logging_conf) -> None:
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		generate = client.assistant.conversation(
			assistant_id='659e54b1b8006379b4b2abd6',
			messages=[
				{
					'role': 'user',
					'content': [{'type': 'text', 'text': "Help me search for the release date of Z.ai's CogVideoX"}],
				}
			],
			stream=True,
			attachments=None,
			metadata=None,
			request_id='request_1790291013237211136',
			user_id='12345678',
		)
		for assistant in generate:
			print(assistant)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_assistant_query_support(logging_conf) -> None:
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.assistant.query_support(
			assistant_id_list=[],
			request_id='request_1790291013237211136',
			user_id='12345678',
		)
		print(response)

	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_assistant_query_conversation_usage(logging_conf) -> None:
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		response = client.assistant.query_conversation_usage(
			assistant_id='659e54b1b8006379b4b2abd6',
			request_id='request_1790291013237211136',
			user_id='12345678',
		)
		print(response)
	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)


def test_translate_api(logging_conf) -> None:
	logging.config.dictConfig(logging_conf)  # type: ignore
	client = ZaiClient()  # Fill in your own API Key
	try:
		translate_response = client.assistant.conversation(
			assistant_id='9996ijk789lmn012o345p999',
			messages=[{'role': 'user', 'content': [{'type': 'text', 'text': 'hello'}]}],
			stream=True,
			attachments=None,
			metadata=None,
			request_id='request_1790291013237211136',
			user_id='12345678',
			extra_parameters={'translate': {'from': 'zh', 'to': 'en'}},
		)
		for chunk in translate_response:
			print(chunk.choices[0].delta)
		# print(translate_response)
	except zai.core._errors.APIRequestFailedError as err:
		print(err)
	except zai.core._errors.APIInternalError as err:
		print(err)
	except zai.core._errors.APIStatusError as err:
		print(err)
