# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 355
- HTTP: 311 alive / 70 gold
- HTTPS: 212 alive / 13 gold
- SOCKS4: 213 alive / 124 gold
- SOCKS5: 229 alive / 148 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20315
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
