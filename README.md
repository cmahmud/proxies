# SyndProxy private pool

## Current pool

- Alive now: 762
- Gold now: 401
- HTTP: 202 alive / 82 gold
- HTTPS: 133 alive / 19 gold
- SOCKS4: 212 alive / 145 gold
- SOCKS5: 215 alive / 155 gold

## Historical pool

- Discovered: 147728
- Ever alive: 25993
- Ever gold: 1077

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
