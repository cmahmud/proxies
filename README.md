# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 417
- HTTP: 80 alive / 64 gold
- HTTPS: 46 alive / 22 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47075
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
