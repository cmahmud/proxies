# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 534
- HTTP: 347 alive / 155 gold
- HTTPS: 257 alive / 97 gold
- SOCKS4: 213 alive / 148 gold
- SOCKS5: 210 alive / 134 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19902
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
