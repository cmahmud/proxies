# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 401
- HTTP: 290 alive / 92 gold
- HTTPS: 223 alive / 33 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 240 alive / 128 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30995
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
