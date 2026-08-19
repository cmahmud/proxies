# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 488
- HTTP: 323 alive / 118 gold
- HTTPS: 197 alive / 70 gold
- SOCKS4: 231 alive / 145 gold
- SOCKS5: 245 alive / 155 gold

## Historical pool

- Discovered: 113571
- Ever alive: 16825
- Ever gold: 624

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
