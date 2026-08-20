# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 347
- HTTP: 187 alive / 65 gold
- HTTPS: 98 alive / 14 gold
- SOCKS4: 191 alive / 135 gold
- SOCKS5: 188 alive / 133 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25789
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
