# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 393
- HTTP: 108 alive / 63 gold
- HTTPS: 43 alive / 15 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 175438
- Ever alive: 33149
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
