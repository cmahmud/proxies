# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 376
- HTTP: 95 alive / 54 gold
- HTTPS: 41 alive / 21 gold
- SOCKS4: 154 alive / 150 gold
- SOCKS5: 161 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43644
- Ever gold: 1375

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
