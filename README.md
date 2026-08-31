# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 464
- HTTP: 130 alive / 94 gold
- HTTPS: 135 alive / 32 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 216 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46013
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
