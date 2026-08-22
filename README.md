# SyndProxy private pool

## Current pool

- Alive now: 917
- Gold now: 444
- HTTP: 238 alive / 98 gold
- HTTPS: 177 alive / 29 gold
- SOCKS4: 236 alive / 151 gold
- SOCKS5: 266 alive / 166 gold

## Historical pool

- Discovered: 163276
- Ever alive: 31803
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
