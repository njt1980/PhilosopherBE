from typing import Dict, List
from pydantic import Field,BaseModel
from langchain.output_parsers import PydanticOutputParser;

class ResponseModel(BaseModel):
    summary: str = Field(description="Summary, no quotes");
    quote: str = Field(description = "relevant quote");
    source: str= Field(description = "source of relevant quote");
    link: str =Field(description = "link to subject");

    def to_dict(self):
        return {
            "summary":self.summary,
            "quote":self.quote,
            "source":self.source,
            "link":self.link,
        }
    
pydantic_output_parser = PydanticOutputParser(pydantic_object=ResponseModel);

