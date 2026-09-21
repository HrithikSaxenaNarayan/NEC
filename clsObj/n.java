public class n {
    public static class phone {
        String brand;
        String model;
        int ram;
        int btry;

        phone (String brand, String model, int ram, int btry) {
            this.brand = brand;
            this.model = model;
            this.ram = ram;
            this.btry = btry;
        }

        phone (String brand, String model, int btry) {
            this.brand = brand;
            this.model = model;
            this.btry = btry;
        }

        phone() {

        }
        @Override 
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("\n Brand: " + this.brand);
            sb.append("\n Model: " + this.model);
            sb.append("\n Ram: " + this.ram);
            sb.append("\n Battery: " + this.btry);
            return sb.toString();
        }
    }

    public static void main(String[] args) {
        phone ph1 = new phone("mi", "xyz", 8, 7000);

        phone iPh = new phone("iphone", "17Pro", 6000);
        phone ph2 = new phone();
        System.out.println(ph1);
    }
}
