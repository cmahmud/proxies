# SyndProxy private pool

## Current pool

- Alive now: 1091
- Gold now: 525
- HTTP: 435 alive / 181 gold
- HTTPS: 267 alive / 99 gold
- SOCKS4: 198 alive / 117 gold
- SOCKS5: 191 alive / 128 gold

## Historical pool

- Discovered: 124851
- Ever alive: 19406
- Ever gold: 772

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
