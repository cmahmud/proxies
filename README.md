# SyndProxy private pool

## Current pool

- Alive now: 811
- Gold now: 214
- HTTP: 224 alive / 24 gold
- HTTPS: 170 alive / 8 gold
- SOCKS4: 195 alive / 98 gold
- SOCKS5: 222 alive / 84 gold

## Historical pool

- Discovered: 91698
- Ever alive: 8633
- Ever gold: 354

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
