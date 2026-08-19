# SyndProxy private pool

## Current pool

- Alive now: 1201
- Gold now: 409
- HTTP: 392 alive / 93 gold
- HTTPS: 258 alive / 14 gold
- SOCKS4: 233 alive / 150 gold
- SOCKS5: 318 alive / 152 gold

## Historical pool

- Discovered: 131841
- Ever alive: 21182
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
