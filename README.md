# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 393
- HTTP: 282 alive / 86 gold
- HTTPS: 227 alive / 29 gold
- SOCKS4: 242 alive / 146 gold
- SOCKS5: 246 alive / 132 gold

## Historical pool

- Discovered: 160991
- Ever alive: 30898
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
