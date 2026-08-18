# SyndProxy private pool

## Current pool

- Alive now: 721
- Gold now: 253
- HTTP: 189 alive / 23 gold
- HTTPS: 119 alive / 2 gold
- SOCKS4: 205 alive / 119 gold
- SOCKS5: 208 alive / 109 gold

## Historical pool

- Discovered: 99103
- Ever alive: 11478
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
