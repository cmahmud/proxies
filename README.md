# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 418
- HTTP: 98 alive / 64 gold
- HTTPS: 95 alive / 22 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35579
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
