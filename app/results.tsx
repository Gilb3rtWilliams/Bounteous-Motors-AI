import { Ionicons } from "@expo/vector-icons";
import { router } from "expo-router";
import { ScrollView, StyleSheet, Text, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

import PrimaryButton from "../src/components/PrimaryButton";
import ReportCard from "../src/components/ReportCard";
import { Colors } from "../src/theme/colors";

export default function ResultsScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView
        contentContainerStyle={styles.content}
        showsVerticalScrollIndicator={false}
      >
        <Text style={styles.header}>AI Valuation Report</Text>

        <Text style={styles.subHeader}>
          Your vehicle has been successfully analyzed.
        </Text>

        <View style={styles.priceCard}>
          <Text style={styles.priceLabel}>Estimated Market Value</Text>

          <Text style={styles.price}>KES 2,450,000</Text>

          <View style={styles.badge}>
            <Ionicons name="shield-checkmark" size={18} color="#fff" />

            <Text style={styles.badgeText}>96.8% Confidence</Text>
          </View>
        </View>

        <ReportCard title="Vehicle Summary">
          <Text style={styles.item}>Manufacturer: Toyota</Text>

          <Text style={styles.item}>Model: Corolla</Text>

          <Text style={styles.item}>Year: 2020</Text>

          <Text style={styles.item}>Mileage: 85,000 km</Text>

          <Text style={styles.item}>Fuel: Petrol</Text>

          <Text style={styles.item}>Transmission: Automatic</Text>
        </ReportCard>

        <ReportCard title="Price Analysis">
          <View style={styles.analysisRow}>
            <Ionicons
              name="checkmark-circle"
              size={20}
              color={Colors.success}
            />

            <Text style={styles.analysisText}>Fair Market Value</Text>
          </View>

          <Text style={styles.range}>Expected Range</Text>

          <Text style={styles.rangeValue}>KES 2,300,000 – KES 2,600,000</Text>
        </ReportCard>

        <ReportCard title="Key Pricing Factors">
          <View style={styles.factor}>
            <Ionicons
              name="checkmark-circle"
              size={20}
              color={Colors.success}
            />
            <Text style={styles.factorText}>Excellent Condition</Text>
          </View>

          <View style={styles.factor}>
            <Ionicons
              name="checkmark-circle"
              size={20}
              color={Colors.success}
            />
            <Text style={styles.factorText}>Low Mileage</Text>
          </View>

          <View style={styles.factor}>
            <Ionicons
              name="checkmark-circle"
              size={20}
              color={Colors.success}
            />
            <Text style={styles.factorText}>Automatic Transmission</Text>
          </View>

          <View style={styles.factor}>
            <Ionicons
              name="checkmark-circle"
              size={20}
              color={Colors.success}
            />
            <Text style={styles.factorText}>Strong Market Demand</Text>
          </View>
        </ReportCard>

        <PrimaryButton
          title="Predict Another Vehicle"
          onPress={() => router.replace("/")}
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

  header: {
    color: Colors.text,
    fontSize: 30,
    fontWeight: "700",
  },

  subHeader: {
    color: Colors.textSecondary,
    marginTop: 8,
    marginBottom: 24,
    fontSize: 16,
  },

  priceCard: {
    backgroundColor: Colors.primary,
    borderRadius: 20,
    padding: 28,
    alignItems: "center",
    marginBottom: 24,
  },

  priceLabel: {
    color: "#fff",
    fontSize: 16,
  },

  price: {
    color: "#fff",
    fontSize: 38,
    fontWeight: "800",
    marginVertical: 12,
  },

  badge: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "rgba(255,255,255,0.15)",
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 20,
  },

  badgeText: {
    color: "#fff",
    marginLeft: 8,
    fontWeight: "600",
  },

  item: {
    color: Colors.text,
    marginBottom: 8,
    fontSize: 15,
  },

  analysisRow: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 16,
  },

  analysisText: {
    color: Colors.text,
    marginLeft: 10,
    fontWeight: "600",
    fontSize: 16,
  },

  range: {
    color: Colors.textSecondary,
    fontSize: 14,
  },

  rangeValue: {
    color: Colors.text,
    fontSize: 20,
    fontWeight: "700",
    marginTop: 6,
  },

  factor: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 12,
  },

  factorText: {
    color: Colors.text,
    marginLeft: 10,
    fontSize: 16,
  },
});
