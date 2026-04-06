import { defineStore } from 'pinia'
import { configApi } from '@/api'

export const useConfigStore = defineStore('config', {
  state: () => ({
    cipher: 'AES',
    target: 'original',
    aim: 'original',
    targets: []
  }),

  actions: {
    async loadTargets() {
      try {
        const response = await configApi.getTargets(this.cipher)
        this.targets = response.data.targets
      } catch (error) {
        console.error('Failed to load targets:', error)
        this.targets = this.cipher === 'AES' 
          ? ['original', 'preload', 'constant_time', 'lut_p', 'custom']
          : ['original', 'preload', 'lut_p', 'custom']
      }
    },

    async setConfig(cipher, target) {
      try {
        const response = await configApi.setConfig({ cipher, target })
        if (response.data.success) {
          this.cipher = response.data.config.cipher
          this.target = response.data.config.target
          this.aim = response.data.config.aim
        }
        return response.data
      } catch (error) {
        console.error('Failed to set config:', error)
        return { success: false }
      }
    },

    async loadConfig() {
      try {
        const response = await configApi.getConfig()
        this.cipher = response.data.cipher
        this.target = response.data.target
        this.aim = response.data.aim
        await this.loadTargets()
      } catch (error) {
        console.error('Failed to load config:', error)
        await this.loadTargets()
      }
    }
  }
})
