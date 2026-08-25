# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 394
- HTTP: 91 alive / 62 gold
- HTTPS: 77 alive / 18 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 168 alive / 157 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37421
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
