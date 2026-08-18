# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 275
- HTTP: 293 alive / 36 gold
- HTTPS: 140 alive / 7 gold
- SOCKS4: 229 alive / 137 gold
- SOCKS5: 165 alive / 95 gold

## Historical pool

- Discovered: 102901
- Ever alive: 13919
- Ever gold: 432

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
