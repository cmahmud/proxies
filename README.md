# SyndProxy private pool

## Current pool

- Alive now: 1151
- Gold now: 399
- HTTP: 359 alive / 91 gold
- HTTPS: 250 alive / 17 gold
- SOCKS4: 235 alive / 145 gold
- SOCKS5: 307 alive / 146 gold

## Historical pool

- Discovered: 133968
- Ever alive: 21759
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
