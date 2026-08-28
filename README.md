# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 421
- HTTP: 92 alive / 71 gold
- HTTPS: 101 alive / 21 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 180 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42558
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
