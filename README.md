# SyndProxy private pool

## Current pool

- Alive now: 1076
- Gold now: 298
- HTTP: 397 alive / 60 gold
- HTTPS: 259 alive / 19 gold
- SOCKS4: 212 alive / 115 gold
- SOCKS5: 208 alive / 104 gold

## Historical pool

- Discovered: 109987
- Ever alive: 15593
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
