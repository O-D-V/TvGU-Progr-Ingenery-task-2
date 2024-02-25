import org.example.Main;
import org.example.Prostoe;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ProstoeTest {
    @Test
    public void prostoe(){
        Prostoe prostoe = new Prostoe() ;
        assertEquals(false, prostoe.prostoe(4));
        assertEquals(true, prostoe.prostoe(5));
        assertEquals(false, prostoe.prostoe(5));//Здесь тест завалится (строка 13)
    }
}
