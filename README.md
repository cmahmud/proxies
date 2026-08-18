# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 241
- HTTP: 323 alive / 29 gold
- HTTPS: 135 alive / 9 gold
- SOCKS4: 248 alive / 115 gold
- SOCKS5: 231 alive / 88 gold

## Historical pool

- Discovered: 86712
- Ever alive: 6880
- Ever gold: 322

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
