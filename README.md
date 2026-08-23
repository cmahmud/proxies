# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 393
- HTTP: 106 alive / 62 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 168 alive / 154 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 175438
- Ever alive: 33149
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
