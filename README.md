# SyndProxy private pool

## Current pool

- Alive now: 956
- Gold now: 298
- HTTP: 365 alive / 65 gold
- HTTPS: 218 alive / 16 gold
- SOCKS4: 194 alive / 117 gold
- SOCKS5: 179 alive / 100 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15616
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
