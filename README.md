# SyndProxy private pool

## Current pool

- Alive now: 1065
- Gold now: 405
- HTTP: 331 alive / 80 gold
- HTTPS: 227 alive / 18 gold
- SOCKS4: 271 alive / 149 gold
- SOCKS5: 236 alive / 158 gold

## Historical pool

- Discovered: 131098
- Ever alive: 20514
- Ever gold: 868

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
