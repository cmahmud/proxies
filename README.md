# SyndProxy private pool

## Current pool

- Alive now: 1035
- Gold now: 525
- HTTP: 359 alive / 153 gold
- HTTPS: 247 alive / 89 gold
- SOCKS4: 222 alive / 148 gold
- SOCKS5: 207 alive / 135 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17709
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
