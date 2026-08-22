# SyndProxy private pool

## Current pool

- Alive now: 1095
- Gold now: 442
- HTTP: 371 alive / 98 gold
- HTTPS: 255 alive / 36 gold
- SOCKS4: 208 alive / 139 gold
- SOCKS5: 261 alive / 169 gold

## Historical pool

- Discovered: 161410
- Ever alive: 31131
- Ever gold: 1155

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
