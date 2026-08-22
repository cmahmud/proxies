# SyndProxy private pool

## Current pool

- Alive now: 910
- Gold now: 406
- HTTP: 284 alive / 97 gold
- HTTPS: 216 alive / 31 gold
- SOCKS4: 185 alive / 124 gold
- SOCKS5: 225 alive / 154 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31086
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
