# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 344
- HTTP: 339 alive / 69 gold
- HTTPS: 255 alive / 18 gold
- SOCKS4: 239 alive / 141 gold
- SOCKS5: 213 alive / 116 gold

## Historical pool

- Discovered: 110913
- Ever alive: 16082
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
