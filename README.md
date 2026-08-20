# SyndProxy private pool

## Current pool

- Alive now: 914
- Gold now: 390
- HTTP: 306 alive / 78 gold
- HTTPS: 184 alive / 22 gold
- SOCKS4: 189 alive / 126 gold
- SOCKS5: 235 alive / 164 gold

## Historical pool

- Discovered: 151047
- Ever alive: 27129
- Ever gold: 1092

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
