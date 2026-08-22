# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 372
- HTTP: 338 alive / 89 gold
- HTTPS: 239 alive / 28 gold
- SOCKS4: 189 alive / 119 gold
- SOCKS5: 221 alive / 136 gold

## Historical pool

- Discovered: 165018
- Ever alive: 32267
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
