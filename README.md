# SyndProxy private pool

## Current pool

- Alive now: 1281
- Gold now: 477
- HTTP: 455 alive / 132 gold
- HTTPS: 336 alive / 76 gold
- SOCKS4: 232 alive / 122 gold
- SOCKS5: 258 alive / 147 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17274
- Ever gold: 629

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
