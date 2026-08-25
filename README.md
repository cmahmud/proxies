# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 416
- HTTP: 119 alive / 68 gold
- HTTPS: 106 alive / 19 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35281
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
