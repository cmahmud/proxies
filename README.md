# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 313
- HTTP: 371 alive / 39 gold
- HTTPS: 174 alive / 10 gold
- SOCKS4: 234 alive / 137 gold
- SOCKS5: 228 alive / 127 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14375
- Ever gold: 440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
