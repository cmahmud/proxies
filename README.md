# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 364
- HTTP: 77 alive / 59 gold
- HTTPS: 73 alive / 7 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 168 alive / 147 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43347
- Ever gold: 1370

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
