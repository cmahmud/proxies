# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 416
- HTTP: 294 alive / 90 gold
- HTTPS: 209 alive / 22 gold
- SOCKS4: 210 alive / 142 gold
- SOCKS5: 241 alive / 162 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29445
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
