# SyndProxy private pool

## Current pool

- Alive now: 1294
- Gold now: 417
- HTTP: 457 alive / 95 gold
- HTTPS: 285 alive / 19 gold
- SOCKS4: 248 alive / 142 gold
- SOCKS5: 304 alive / 161 gold

## Historical pool

- Discovered: 131823
- Ever alive: 20961
- Ever gold: 877

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
