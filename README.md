# SyndProxy private pool

## Current pool

- Alive now: 884
- Gold now: 471
- HTTP: 265 alive / 123 gold
- HTTPS: 214 alive / 86 gold
- SOCKS4: 181 alive / 123 gold
- SOCKS5: 224 alive / 139 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17497
- Ever gold: 668

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
