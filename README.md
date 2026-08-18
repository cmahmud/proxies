# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 243
- HTTP: 466 alive / 31 gold
- HTTPS: 167 alive / 7 gold
- SOCKS4: 220 alive / 111 gold
- SOCKS5: 223 alive / 94 gold

## Historical pool

- Discovered: 91719
- Ever alive: 9072
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
