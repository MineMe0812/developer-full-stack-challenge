<template>
    <b-container align-v="center">
        <b-navbar toggleable="lg" type="light">
            <b-navbar-brand>
                <NuxtLink to="/"><b-img src="../assets/images/logo.svg" alt="DataCose Logo" class="pl-10" style="height: 40px;" /></NuxtLink>
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <!-- Right aligned nav items -->
                <b-navbar-nav class="ml-auto">

                    <b-nav-item>
                        <NuxtLink to="/">Authors</NuxtLink>
                    </b-nav-item>
                    <b-nav-item>
                        <NuxtLink to="/book">Books</NuxtLink>
                    </b-nav-item>

                    <b-nav-item-dropdown right>
                        <!-- Using 'button-content' slot -->
                        <template #button-content>
                            <em>User</em>
                        </template>
                        <b-dropdown-item><router-link to="/login">Sign Out</router-link></b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </b-container>
</template>

<style lang="scss">
/* home route and active route will show in bold as it matches / and /about */
a.nuxt-link-active {
    font-weight: bold;
}

/* exact link will show the primary color for only the exact matching link */
a.nuxt-link-exact-active {
    color: #00c58e;
}
</style>