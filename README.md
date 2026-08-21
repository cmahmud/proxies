# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 401
- HTTP: 291 alive / 94 gold
- HTTPS: 199 alive / 33 gold
- SOCKS4: 234 alive / 146 gold
- SOCKS5: 232 alive / 128 gold

## Historical pool

- Discovered: 161006
- Ever alive: 30989
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
