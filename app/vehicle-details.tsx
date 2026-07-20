import { router } from "expo-router";
import { useState } from "react";
import { ScrollView, StyleSheet, Text, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

import FormField from "../src/components/FormField";
import PrimaryButton from "../src/components/PrimaryButton";
import { Colors } from "../src/theme/colors";

export default function VehicleDetails() {
  const [manufacturer, setManufacturer] = useState("Toyota");
  const [model, setModel] = useState("");
  const [year, setYear] = useState("2020");
  const [mileage, setMileage] = useState("");
  const [fuel, setFuel] = useState("Petrol");
  const [transmission, setTransmission] = useState("Automatic");
  const [condition, setCondition] = useState("Excellent");

  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        contentContainerStyle={styles.content}
        showsVerticalScrollIndicator={false}
      >
        <Text style={styles.title}>Vehicle Information</Text>

        <Text style={styles.subtitle}>
          Tell us about the vehicle. Our AI will use this information to
          estimate its market value.
        </Text>

        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Basic Information</Text>

          <FormField
            label="Manufacturer"
            icon="car-sport"
            type="picker"
            value={manufacturer}
            onValueChange={setManufacturer}
            items={[
              { label: "Toyota", value: "Toyota" },
              { label: "Honda", value: "Honda" },
              { label: "Nissan", value: "Nissan" },
              { label: "BMW", value: "BMW" },
              { label: "Mercedes-Benz", value: "Mercedes-Benz" },
            ]}
          />

          <FormField
            label="Model"
            icon="pricetag"
            value={model}
            placeholder="e.g. Corolla"
            onChangeText={setModel}
          />

          <FormField
            label="Year"
            icon="calendar"
            type="picker"
            value={year}
            onValueChange={setYear}
            items={[
              { label: "2024", value: "2024" },
              { label: "2023", value: "2023" },
              { label: "2022", value: "2022" },
              { label: "2021", value: "2021" },
              { label: "2020", value: "2020" },
            ]}
          />
        </View>

        <View style={styles.section}>
          <Text style={styles.sectionTitle}>Specifications</Text>

          <FormField
            label="Mileage"
            icon="speedometer"
            value={mileage}
            keyboardType="numeric"
            placeholder="Enter mileage"
            onChangeText={setMileage}
          />

          <FormField
            label="Fuel Type"
            icon="water"
            type="picker"
            value={fuel}
            onValueChange={setFuel}
            items={[
              { label: "Petrol", value: "Petrol" },
              { label: "Diesel", value: "Diesel" },
              { label: "Hybrid", value: "Hybrid" },
              { label: "Electric", value: "Electric" },
            ]}
          />

          <FormField
            label="Transmission"
            icon="settings"
            type="picker"
            value={transmission}
            onValueChange={setTransmission}
            items={[
              { label: "Automatic", value: "Automatic" },
              { label: "Manual", value: "Manual" },
            ]}
          />

          <FormField
            label="Condition"
            icon="star"
            type="picker"
            value={condition}
            onValueChange={setCondition}
            items={[
              { label: "Excellent", value: "Excellent" },
              { label: "Good", value: "Good" },
              { label: "Fair", value: "Fair" },
              { label: "Poor", value: "Poor" },
            ]}
          />
        </View>

        <PrimaryButton
          title="Continue"
          onPress={() => router.push("/upload-images")}
        />
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.background,
  },

  content: {
    padding: 24,
    paddingBottom: 40,
  },

  title: {
    color: Colors.text,
    fontSize: 30,
    fontWeight: "700",
    marginBottom: 8,
  },

  subtitle: {
    color: Colors.textSecondary,
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 32,
  },

  section: {
    marginBottom: 32,
  },

  sectionTitle: {
    color: Colors.primary,
    fontSize: 18,
    fontWeight: "700",
    marginBottom: 16,
  },
});
