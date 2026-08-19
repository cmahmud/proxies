# SyndProxy private pool

## Current pool

- Alive now: 1196
- Gold now: 388
- HTTP: 389 alive / 91 gold
- HTTPS: 270 alive / 19 gold
- SOCKS4: 237 alive / 137 gold
- SOCKS5: 300 alive / 141 gold

## Historical pool

- Discovered: 133961
- Ever alive: 21624
- Ever gold: 886

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
