# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 418
- HTTP: 83 alive / 62 gold
- HTTPS: 74 alive / 27 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47129
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
