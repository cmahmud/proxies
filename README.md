# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 423
- HTTP: 101 alive / 78 gold
- HTTPS: 106 alive / 19 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42096
- Ever gold: 1350

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
