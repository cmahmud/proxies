# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 215
- HTTP: 306 alive / 34 gold
- HTTPS: 169 alive / 10 gold
- SOCKS4: 213 alive / 98 gold
- SOCKS5: 199 alive / 73 gold

## Historical pool

- Discovered: 86648
- Ever alive: 5725
- Ever gold: 290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
