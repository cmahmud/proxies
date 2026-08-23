# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 393
- HTTP: 110 alive / 64 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33149
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
