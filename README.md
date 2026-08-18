# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 213
- HTTP: 522 alive / 36 gold
- HTTPS: 199 alive / 10 gold
- SOCKS4: 197 alive / 96 gold
- SOCKS5: 185 alive / 71 gold

## Historical pool

- Discovered: 82966
- Ever alive: 5655
- Ever gold: 287

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
