# SyndProxy private pool

## Current pool

- Alive now: 912
- Gold now: 377
- HTTP: 256 alive / 89 gold
- HTTPS: 224 alive / 24 gold
- SOCKS4: 205 alive / 122 gold
- SOCKS5: 227 alive / 142 gold

## Historical pool

- Discovered: 164245
- Ever alive: 32068
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
