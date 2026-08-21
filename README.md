# SyndProxy private pool

## Current pool

- Alive now: 902
- Gold now: 416
- HTTP: 287 alive / 90 gold
- HTTPS: 166 alive / 25 gold
- SOCKS4: 207 alive / 141 gold
- SOCKS5: 242 alive / 160 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29448
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
