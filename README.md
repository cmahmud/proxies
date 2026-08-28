# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 428
- HTTP: 103 alive / 81 gold
- HTTPS: 134 alive / 19 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42423
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
