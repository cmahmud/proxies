# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 403
- HTTP: 102 alive / 72 gold
- HTTPS: 57 alive / 22 gold
- SOCKS4: 166 alive / 153 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48095
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
