# SyndProxy private pool

## Current pool

- Alive now: 767
- Gold now: 395
- HTTP: 227 alive / 89 gold
- HTTPS: 117 alive / 26 gold
- SOCKS4: 185 alive / 122 gold
- SOCKS5: 238 alive / 158 gold

## Historical pool

- Discovered: 156423
- Ever alive: 29477
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
