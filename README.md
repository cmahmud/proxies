# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 458
- HTTP: 433 alive / 118 gold
- HTTPS: 284 alive / 72 gold
- SOCKS4: 229 alive / 140 gold
- SOCKS5: 224 alive / 128 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16750
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
