# SyndProxy private pool

## Current pool

- Alive now: 1089
- Gold now: 534
- HTTP: 401 alive / 160 gold
- HTTPS: 258 alive / 89 gold
- SOCKS4: 204 alive / 140 gold
- SOCKS5: 226 alive / 145 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18648
- Ever gold: 723

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
