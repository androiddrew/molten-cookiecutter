from molten import schema, field


@schema
class Link:
    href: str


@schema
class APIResponse:
    status: int = field(description="An HTTP status code")
    message: str = field(
        description="A user presentable message in response to the request provided to the API"
    )
