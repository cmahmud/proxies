# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 418
- HTTP: 90 alive / 63 gold
- HTTPS: 73 alive / 19 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 185 alive / 174 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35606
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
