# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 405
- HTTP: 89 alive / 63 gold
- HTTPS: 88 alive / 16 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 194 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39258
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
