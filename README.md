# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 433
- HTTP: 131 alive / 78 gold
- HTTPS: 104 alive / 23 gold
- SOCKS4: 180 alive / 162 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34474
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
