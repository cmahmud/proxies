# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 466
- HTTP: 130 alive / 96 gold
- HTTPS: 130 alive / 34 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 217 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46048
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
