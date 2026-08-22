# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 381
- HTTP: 345 alive / 85 gold
- HTTPS: 235 alive / 27 gold
- SOCKS4: 230 alive / 124 gold
- SOCKS5: 233 alive / 145 gold

## Historical pool

- Discovered: 164181
- Ever alive: 32046
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
