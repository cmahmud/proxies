# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 383
- HTTP: 100 alive / 53 gold
- HTTPS: 29 alive / 10 gold
- SOCKS4: 165 alive / 158 gold
- SOCKS5: 178 alive / 162 gold

## Historical pool

- Discovered: 179377
- Ever alive: 33459
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
