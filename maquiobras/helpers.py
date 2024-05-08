DEFAULT_TYPE_FORMATTER = {
    "datetime": lambda val: val.strftime("%Y-%m-%d %H:%M:%S") if val else val,
    "Decimal": lambda val: float(val)
}



class BaseSerializer(object):
    fields = None
    fields_format = {}
    fields_by_type = DEFAULT_TYPE_FORMATTER

    def serialize(self):
        if not self.fields:
            raise NotImplementedError("Please add a fields attr to your class")
        data = {}
        for f in self.fields:
            value = getattr(self, f)
            type_str = type(value).__name__
            type_formatter = self.fields_by_type.get(type_str, None)
            field_formatter = self.fields_format.get(f, None)
            if type_formatter:
                formatter = type_formatter
            elif field_formatter:
                formatter = field_formatter
            else:
                def formatter(x): return x
            data[f] = formatter(value) if formatter else value
        return data
