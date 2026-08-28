# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 384
- HTTP: 79 alive / 54 gold
- HTTPS: 37 alive / 14 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 186 alive / 156 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42855
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
