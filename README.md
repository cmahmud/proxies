# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 405
- HTTP: 76 alive / 60 gold
- HTTPS: 56 alive / 21 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42801
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
