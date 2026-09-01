# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 421
- HTTP: 79 alive / 66 gold
- HTTPS: 83 alive / 26 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47144
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
