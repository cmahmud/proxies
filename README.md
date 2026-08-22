# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 419
- HTTP: 354 alive / 100 gold
- HTTPS: 237 alive / 31 gold
- SOCKS4: 203 alive / 135 gold
- SOCKS5: 227 alive / 153 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31091
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
