# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 405
- HTTP: 72 alive / 56 gold
- HTTPS: 73 alive / 23 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42775
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
