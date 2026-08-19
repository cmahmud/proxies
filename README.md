# SyndProxy private pool

## Current pool

- Alive now: 1072
- Gold now: 546
- HTTP: 384 alive / 159 gold
- HTTPS: 273 alive / 107 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 208 alive / 147 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19836
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
