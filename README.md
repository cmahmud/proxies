# SyndProxy private pool

## Current pool

- Alive now: 1648
- Gold now: 656
- HTTP: 652 alive / 219 gold
- HTTPS: 513 alive / 110 gold
- SOCKS4: 227 alive / 158 gold
- SOCKS5: 256 alive / 169 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23936
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
