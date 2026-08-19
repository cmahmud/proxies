# SyndProxy private pool

## Current pool

- Alive now: 1028
- Gold now: 534
- HTTP: 347 alive / 157 gold
- HTTPS: 257 alive / 93 gold
- SOCKS4: 212 alive / 149 gold
- SOCKS5: 212 alive / 135 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19902
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
