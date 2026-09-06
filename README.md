# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 360
- HTTP: 68 alive / 51 gold
- HTTPS: 29 alive / 12 gold
- SOCKS4: 160 alive / 151 gold
- SOCKS5: 172 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48255
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
