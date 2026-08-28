# SyndProxy validated proxy pool

## Current pool

- Alive now: 595
- Gold now: 426
- HTTP: 107 alive / 80 gold
- HTTPS: 126 alive / 19 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42424
- Ever gold: 1355

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
