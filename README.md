# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 479
- HTTP: 371 alive / 136 gold
- HTTPS: 227 alive / 90 gold
- SOCKS4: 224 alive / 138 gold
- SOCKS5: 209 alive / 115 gold

## Historical pool

- Discovered: 117111
- Ever alive: 17417
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
