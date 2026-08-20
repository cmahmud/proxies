# SyndProxy private pool

## Current pool

- Alive now: 790
- Gold now: 420
- HTTP: 199 alive / 80 gold
- HTTPS: 154 alive / 29 gold
- SOCKS4: 218 alive / 151 gold
- SOCKS5: 219 alive / 160 gold

## Historical pool

- Discovered: 151059
- Ever alive: 27323
- Ever gold: 1094

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
