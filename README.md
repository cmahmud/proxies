# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 432
- HTTP: 114 alive / 82 gold
- HTTPS: 136 alive / 19 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 193 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42284
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
