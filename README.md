# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 396
- HTTP: 101 alive / 61 gold
- HTTPS: 59 alive / 14 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
