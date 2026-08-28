# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 398
- HTTP: 80 alive / 60 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 177 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42831
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
