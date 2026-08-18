# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 227
- HTTP: 268 alive / 29 gold
- HTTPS: 153 alive / 8 gold
- SOCKS4: 248 alive / 109 gold
- SOCKS5: 218 alive / 81 gold

## Historical pool

- Discovered: 86774
- Ever alive: 7592
- Ever gold: 337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
