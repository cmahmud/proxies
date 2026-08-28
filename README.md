# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 408
- HTTP: 80 alive / 59 gold
- HTTPS: 79 alive / 22 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 195 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42727
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
