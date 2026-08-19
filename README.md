# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 494
- HTTP: 320 alive / 117 gold
- HTTPS: 196 alive / 70 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 239 alive / 159 gold

## Historical pool

- Discovered: 113571
- Ever alive: 16824
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
