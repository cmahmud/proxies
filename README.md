# SyndProxy private pool

## Current pool

- Alive now: 1014
- Gold now: 475
- HTTP: 311 alive / 121 gold
- HTTPS: 218 alive / 70 gold
- SOCKS4: 226 alive / 136 gold
- SOCKS5: 259 alive / 148 gold

## Historical pool

- Discovered: 113575
- Ever alive: 16862
- Ever gold: 625

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
