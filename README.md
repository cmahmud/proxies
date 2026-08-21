# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 399
- HTTP: 294 alive / 92 gold
- HTTPS: 232 alive / 32 gold
- SOCKS4: 211 alive / 148 gold
- SOCKS5: 231 alive / 127 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30999
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
