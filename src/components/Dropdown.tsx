import { Picker } from "@react-native-picker/picker";
import { StyleSheet, Text, View } from "react-native";
import { Colors } from "../theme/colors";

type Props = {
  label: string;
  selectedValue: string;
  onValueChange: (value: string) => void;
  items: string[];
};

export default function Dropdown({
  label,
  selectedValue,
  onValueChange,
  items,
}: Props) {
  return (
    <View style={styles.container}>
      <Text style={styles.label}>{label}</Text>

      <View style={styles.pickerContainer}>
        <Picker
          selectedValue={selectedValue}
          dropdownIconColor="white"
          onValueChange={onValueChange}
          style={styles.picker}
        >
          {items.map((item) => (
            <Picker.Item key={item} label={item} value={item} />
          ))}
        </Picker>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: 20,
  },

  label: {
    color: Colors.text,
    marginBottom: 8,
    fontSize: 16,
    fontWeight: "600",
  },

  pickerContainer: {
    backgroundColor: Colors.surface,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: Colors.border,
  },

  picker: {
    color: Colors.text,
  },
});
