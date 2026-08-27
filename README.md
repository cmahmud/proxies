# SyndProxy validated proxy pool

## Current pool

- Alive now: 657
- Gold now: 406
- HTTP: 102 alive / 62 gold
- HTTPS: 180 alive / 18 gold
- SOCKS4: 180 alive / 158 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40660
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
