# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 388
- HTTP: 78 alive / 57 gold
- HTTPS: 37 alive / 14 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 185 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42856
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
