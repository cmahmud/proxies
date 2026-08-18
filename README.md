# SyndProxy private pool

## Current pool

- Alive now: 568
- Gold now: 225
- HTTP: 138 alive / 26 gold
- HTTPS: 76 alive / 7 gold
- SOCKS4: 159 alive / 110 gold
- SOCKS5: 195 alive / 82 gold

## Historical pool

- Discovered: 91696
- Ever alive: 8361
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
