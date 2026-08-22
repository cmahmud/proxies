# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 402
- HTTP: 287 alive / 93 gold
- HTTPS: 215 alive / 29 gold
- SOCKS4: 232 alive / 146 gold
- SOCKS5: 253 alive / 134 gold

## Historical pool

- Discovered: 161992
- Ever alive: 31312
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
