# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 372
- HTTP: 170 alive / 69 gold
- HTTPS: 144 alive / 12 gold
- SOCKS4: 218 alive / 153 gold
- SOCKS5: 207 alive / 138 gold

## Historical pool

- Discovered: 147685
- Ever alive: 25896
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
