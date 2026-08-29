# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 374
- HTTP: 88 alive / 52 gold
- HTTPS: 43 alive / 22 gold
- SOCKS4: 155 alive / 151 gold
- SOCKS5: 161 alive / 149 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43642
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
