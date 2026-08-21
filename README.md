# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 396
- HTTP: 245 alive / 89 gold
- HTTPS: 131 alive / 19 gold
- SOCKS4: 217 alive / 151 gold
- SOCKS5: 234 alive / 137 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29241
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
