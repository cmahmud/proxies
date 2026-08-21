# SyndProxy private pool

## Current pool

- Alive now: 855
- Gold now: 410
- HTTP: 267 alive / 88 gold
- HTTPS: 159 alive / 24 gold
- SOCKS4: 196 alive / 142 gold
- SOCKS5: 233 alive / 156 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29451
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
