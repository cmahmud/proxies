# SyndProxy validated proxy pool

## Current pool

- Alive now: 669
- Gold now: 463
- HTTP: 134 alive / 94 gold
- HTTPS: 143 alive / 29 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 219 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45995
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
