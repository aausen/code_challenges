class AssemblyLine
    def initialize(speed)
      @speed = speed
    end

    def production_rate_per_hour
      if @speed >= 1 && @speed <= 4
        prod_rate = 221 * @speed
      elsif @speed >= 5 && @speed <= 8
        prod_rate = (221 * @speed) * 0.9
      elsif @speed == 9
        prod_rate = (221 * @speed) * 0.8
      else
        prod_rate = (221 * @speed) * 0.77
      end
      return prod_rate
    end

    def working_items_per_minute
      prod_rate = production_rate_per_hour
      per_min = prod_rate / 60
      return per_min.to_i
    end