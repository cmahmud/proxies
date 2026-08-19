# SyndProxy private pool

## Current pool

- Alive now: 1020
- Gold now: 536
- HTTP: 338 alive / 158 gold
- HTTPS: 258 alive / 94 gold
- SOCKS4: 213 alive / 149 gold
- SOCKS5: 211 alive / 135 gold

## Historical pool

- Discovered: 127371
- Ever alive: 19902
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
