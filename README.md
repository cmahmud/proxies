# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 389
- HTTP: 319 alive / 76 gold
- HTTPS: 213 alive / 12 gold
- SOCKS4: 250 alive / 148 gold
- SOCKS5: 233 alive / 153 gold

## Historical pool

- Discovered: 129305
- Ever alive: 20390
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
