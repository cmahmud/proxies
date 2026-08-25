# SyndProxy validated proxy pool

## Current pool

- Alive now: 580
- Gold now: 421
- HTTP: 115 alive / 72 gold
- HTTPS: 102 alive / 22 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35051
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
