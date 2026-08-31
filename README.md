# SyndProxy validated proxy pool

## Current pool

- Alive now: 664
- Gold now: 462
- HTTP: 131 alive / 94 gold
- HTTPS: 142 alive / 29 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 217 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46002
- Ever gold: 1439

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
