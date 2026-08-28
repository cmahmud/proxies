# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 425
- HTTP: 114 alive / 80 gold
- HTTPS: 141 alive / 20 gold
- SOCKS4: 179 alive / 158 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42379
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
