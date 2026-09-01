# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 418
- HTTP: 82 alive / 62 gold
- HTTPS: 40 alive / 24 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47089
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
