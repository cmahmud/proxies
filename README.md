# SyndProxy private pool

## Current pool

- Alive now: 764
- Gold now: 390
- HTTP: 242 alive / 91 gold
- HTTPS: 101 alive / 21 gold
- SOCKS4: 188 alive / 122 gold
- SOCKS5: 233 alive / 156 gold

## Historical pool

- Discovered: 156417
- Ever alive: 29459
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
