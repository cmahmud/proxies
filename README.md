# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 405
- HTTP: 101 alive / 70 gold
- HTTPS: 59 alive / 25 gold
- SOCKS4: 161 alive / 153 gold
- SOCKS5: 167 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43651
- Ever gold: 1376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
