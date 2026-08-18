# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 248
- HTTP: 406 alive / 32 gold
- HTTPS: 172 alive / 7 gold
- SOCKS4: 237 alive / 114 gold
- SOCKS5: 232 alive / 95 gold

## Historical pool

- Discovered: 91719
- Ever alive: 9080
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
