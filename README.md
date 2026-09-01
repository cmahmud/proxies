# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 418
- HTTP: 85 alive / 67 gold
- HTTPS: 64 alive / 25 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47163
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
