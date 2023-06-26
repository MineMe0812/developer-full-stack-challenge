<template>
    <b-container class="mt-5">
        <b-row>
            <b-button right class="ml-2" variant="primary" v-b-modal.modal-prevent-closing>Add</b-button>
        </b-row>
     
        <b-row class="mb-2" align-h="between">
            <b-col cols="auto" class="my-1">
                <b-form-group label="Per page" label-for="per-page-select" label-cols-sm="6" label-cols-md="6"
                    label-cols-lg="6" label-align-sm="left" label-size="sm" class="mb-0">
                    <b-form-select id="per-page-select" v-model="perPage" :options="pageOptions" size="sm"></b-form-select>
                </b-form-group>
            </b-col>


            <b-col cols="auto" class="my-1">
                <b-form-group label="Filter" label-for="filter-input" label-cols-sm="3" label-align-sm="right"
                    label-size="sm" class="mb-0">
                    <b-input-group size="sm">
                        <b-form-input id="filter-input" v-model="filter" type="search"
                            placeholder="Type to Search"></b-form-input>
                        <b-input-group-append>
                            <b-button :disabled="!filter" @click="filter = ''">Clear</b-button>
                        </b-input-group-append>
                    </b-input-group>
                </b-form-group>
            </b-col>
        </b-row>

        
        <b-table striped hover bordered :items="items" :fields="fields" :current-page="currentPage" :per-page="perPage"
            :filter="filter" show-empty @filtered="onFiltered" @row-clicked="myRowClickHandler">

            <template #cell(name)="row">
                {{ row.value.first }} {{ row.value.last }}
            </template>

            <template #cell(actions)="row">
                <b-button size="sm" variant="danger">Delete</b-button>
            </template>
        </b-table>

        <b-row align-h="between">
            <b-col sm="6" md="6" class="my-1">
            </b-col>
            <b-col cols="auto" class="my-1">
                <b-pagination v-model="currentPage" :total-rows="totalRows" :per-page="perPage" class="my-0"></b-pagination>
            </b-col>
        </b-row>

        
        <b-modal id="modal-prevent-closing" ref="modal" title="Submit Your Name" @show="resetModal" @hidden="resetModal"
            @ok="handleOk">
            <form ref="form" @submit.stop.prevent="handleSubmit">
                <b-form-group label="Name" label-for="name-input" invalid-feedback="Name is required" :state="nameState">
                    <b-form-input id="name-input" v-model="name" :state="nameState" required></b-form-input>
                </b-form-group>
                <b-form-group label="Books" label-for="name-input" >
                    <treeselect v-model="value" :multiple="true" :options="options" />
                </b-form-group>
            </form>
        </b-modal>
    </b-container>
</template>
  
<script>
 // import the component
 import Treeselect from '@riophae/vue-treeselect'
  // import the styles
  import '@riophae/vue-treeselect/dist/vue-treeselect.css'

export default {
    layout: 'main',
    components: { Treeselect },
    data() {
        return {
            items: [
                { isActive: true, age: 40, name: { first: 'Dickerson', last: 'Macdonald' } },
                { isActive: false, age: 21, name: { first: 'Larsen', last: 'Shaw' } },
                { isActive: false, age: 89, name: { first: 'Geneva', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'Jami', last: 'Carney' } },
                { isActive: false, age: 27, name: { first: 'Essie', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Thor', last: 'Macdonald' } },
                { isActive: false, age: 26, name: { first: 'Mitzi', last: 'Navarro' } },
                { isActive: false, age: 22, name: { first: 'Genevieve', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'John', last: 'Carney' } },
                { isActive: false, age: 29, name: { first: 'Dick', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Dickerson', last: 'Macdonald' } },
                { isActive: false, age: 21, name: { first: 'Larsen', last: 'Shaw' } },
                { isActive: false, age: 89, name: { first: 'Geneva', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'Jami', last: 'Carney' } },
                { isActive: false, age: 27, name: { first: 'Essie', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Thor', last: 'Macdonald' } },
                { isActive: false, age: 26, name: { first: 'Mitzi', last: 'Navarro' } },
                { isActive: false, age: 22, name: { first: 'Genevieve', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'John', last: 'Carney' } },
                { isActive: false, age: 29, name: { first: 'Dick', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Dickerson', last: 'Macdonald' } },
                { isActive: false, age: 21, name: { first: 'Larsen', last: 'Shaw' } },
                { isActive: false, age: 89, name: { first: 'Geneva', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'Jami', last: 'Carney' } },
                { isActive: false, age: 27, name: { first: 'Essie', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Thor', last: 'Macdonald' } },
                { isActive: false, age: 26, name: { first: 'Mitzi', last: 'Navarro' } },
                { isActive: false, age: 22, name: { first: 'Genevieve', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'John', last: 'Carney' } },
                { isActive: false, age: 29, name: { first: 'Dick', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Dickerson', last: 'Macdonald' } },
                { isActive: false, age: 21, name: { first: 'Larsen', last: 'Shaw' } },
                { isActive: false, age: 89, name: { first: 'Geneva', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'Jami', last: 'Carney' } },
                { isActive: false, age: 27, name: { first: 'Essie', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Thor', last: 'Macdonald' } },
                { isActive: false, age: 26, name: { first: 'Mitzi', last: 'Navarro' } },
                { isActive: false, age: 22, name: { first: 'Genevieve', last: 'Wilson' } },
                { isActive: true, age: 38, name: { first: 'John', last: 'Carney' } },
                { isActive: false, age: 29, name: { first: 'Dick', last: 'Dunlap' } },
                { isActive: true, age: 40, name: { first: 'Dickerson', last: 'Macdonald' } },
                { isActive: false, age: 21, name: { first: 'Larsen', last: 'Shaw' } },

            ],
            fields: [
                { key: 'name', label: 'Name', sortable: true, sortDirection: 'desc' },
                { key: 'age', label: 'Number of books', sortable: true, class: 'text-center' },
                { key: 'actions', label: 'Actions', class: 'text-center' }
            ],
            totalRows: 1,
            currentPage: 1,
            perPage: 5,
            pageOptions: [5, 10, 15, { value: 100, text: "Show a lot" }],
            sortBy: '',
            sortDesc: false,
            sortDirection: 'asc',
            filter: null,
            filterOn: [],
            infoModal: {
                id: 'info-modal',
                title: '',
                content: ''
            },
            name: '',
            nameState: null,
            submittedNames: [],
            // define the default value
            value: null,
            // define options
            options: [ {
            id: 'a',
            label: 'a',
            children: [ {
                id: 'aa',
                label: 'aa',
            }, {
                id: 'ab',
                label: 'ab',
            } ],
            }, {
            id: 'b',
            label: 'b',
            }, {
            id: 'c',
            label: 'c',
            } ],
        }
    },
    computed: {
        sortOptions() {
            // Create an options list from our fields
            return this.fields
                .filter(f => f.sortable)
                .map(f => {
                    return { text: f.label, value: f.key }
                })
        }
    },
    mounted() {
        // Set the initial number of items
        this.totalRows = this.items.length
    },
    methods: {
        info(item, index, button) {
            this.infoModal.title = `Row index: ${index}`
            this.infoModal.content = JSON.stringify(item, null, 2)
            this.$root.$emit('bv::show::modal', this.infoModal.id, button)
        },
        resetInfoModal() {
            this.infoModal.title = ''
            this.infoModal.content = ''
        },

        onFiltered(filteredItems) {
            // Trigger pagination to update the number of buttons/pages due to filtering
            this.totalRows = filteredItems.length
            this.currentPage = 1
        },
        myRowClickHandler(item, index) {
            this.$bvModal.show('modal-prevent-closing')
        },
        checkFormValidity() {
            const valid = this.$refs.form.checkValidity()
            this.nameState = valid
            return valid
        },
        resetModal() {
            this.name = ''
            this.nameState = null
        },
        handleOk(bvModalEvent) {
            // Prevent modal from closing
            bvModalEvent.preventDefault()
            // Trigger submit handler
            this.handleSubmit()
        },
        handleSubmit() {
            // Exit when the form isn't valid
            if (!this.checkFormValidity()) {
                return
            }
            // Push the name to submitted names
            this.submittedNames.push(this.name)
            // Hide the modal manually
            this.$nextTick(() => {
                this.$bvModal.hide('modal-prevent-closing')
            })
        }
    }
}
</script>