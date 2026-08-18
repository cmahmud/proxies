# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 274
- HTTP: 192 alive / 23 gold
- HTTPS: 118 alive / 2 gold
- SOCKS4: 218 alive / 136 gold
- SOCKS5: 209 alive / 113 gold

## Historical pool

- Discovered: 99103
- Ever alive: 11478
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
