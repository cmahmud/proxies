# SyndProxy private pool

## Current pool

- Alive now: 997
- Gold now: 256
- HTTP: 375 alive / 33 gold
- HTTPS: 180 alive / 4 gold
- SOCKS4: 214 alive / 115 gold
- SOCKS5: 228 alive / 104 gold

## Historical pool

- Discovered: 99105
- Ever alive: 11773
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
