# SyndProxy private pool

## Current pool

- Alive now: 1081
- Gold now: 511
- HTTP: 386 alive / 148 gold
- HTTPS: 275 alive / 89 gold
- SOCKS4: 191 alive / 118 gold
- SOCKS5: 229 alive / 156 gold

## Historical pool

- Discovered: 118126
- Ever alive: 17800
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
