<template>
    <div class="login">
        <b-container id="mainContainer" align-v="center">
            <BlobBg />
            <b-row align-v="center" align-h="center">
                <b-col md="6">
                    <FormLogin />
                </b-col>
                <b-col md="6">
                    <b-img src="../assets/images/business.png" fluid class="businessImg scale-in-bottom" center />
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>
  
<script>

export default {
    
};
</script>
  
<style lang="scss">
    #mainContainer {
        width: 100%;
        height: auto;
        position: relative;
    }

    .login {
        display: flex;
        align-items: center;
        min-height: 100vh;
        /* background: linear-gradient(to right, #41b883, #83c5be); */
        /* background: url('./assets/images/bg.jpg'); */
        background: linear-gradient(to bottom,
                rgba(65, 184, 131, 0.5) 0%,
                rgba(131, 197, 190, 0.5) 100%),
            url("./assets/images/bg.jpg");
        background-position: center;
        background-size: cover;
        padding: 30px 0 0;
    }
</style>