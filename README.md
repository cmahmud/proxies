# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 343
- HTTP: 321 alive / 86 gold
- HTTPS: 251 alive / 29 gold
- SOCKS4: 205 alive / 139 gold
- SOCKS5: 202 alive / 89 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32517
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
