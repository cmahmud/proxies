# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 394
- HTTP: 298 alive / 77 gold
- HTTPS: 170 alive / 25 gold
- SOCKS4: 223 alive / 144 gold
- SOCKS5: 233 alive / 148 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29584
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
