# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 439
- HTTP: 325 alive / 90 gold
- HTTPS: 235 alive / 29 gold
- SOCKS4: 215 alive / 151 gold
- SOCKS5: 258 alive / 169 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31230
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
