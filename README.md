# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 417
- HTTP: 83 alive / 65 gold
- HTTPS: 65 alive / 25 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 182 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47163
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
