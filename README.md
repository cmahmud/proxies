# SyndProxy private pool

## Current pool

- Alive now: 1692
- Gold now: 614
- HTTP: 633 alive / 215 gold
- HTTPS: 484 alive / 115 gold
- SOCKS4: 218 alive / 134 gold
- SOCKS5: 357 alive / 150 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23925
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
