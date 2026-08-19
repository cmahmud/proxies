# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 341
- HTTP: 262 alive / 59 gold
- HTTPS: 189 alive / 15 gold
- SOCKS4: 207 alive / 134 gold
- SOCKS5: 204 alive / 133 gold

## Historical pool

- Discovered: 129236
- Ever alive: 20046
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
