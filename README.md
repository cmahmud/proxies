# SyndProxy private pool

## Current pool

- Alive now: 878
- Gold now: 403
- HTTP: 254 alive / 95 gold
- HTTPS: 177 alive / 25 gold
- SOCKS4: 235 alive / 157 gold
- SOCKS5: 212 alive / 126 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30845
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
