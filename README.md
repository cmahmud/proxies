# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 410
- HTTP: 100 alive / 63 gold
- HTTPS: 90 alive / 20 gold
- SOCKS4: 180 alive / 159 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35468
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
