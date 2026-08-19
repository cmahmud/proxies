# SyndProxy private pool

## Current pool

- Alive now: 1285
- Gold now: 386
- HTTP: 437 alive / 91 gold
- HTTPS: 312 alive / 16 gold
- SOCKS4: 221 alive / 129 gold
- SOCKS5: 315 alive / 150 gold

## Historical pool

- Discovered: 134541
- Ever alive: 22005
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
