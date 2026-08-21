# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 375
- HTTP: 305 alive / 97 gold
- HTTPS: 195 alive / 26 gold
- SOCKS4: 218 alive / 140 gold
- SOCKS5: 209 alive / 112 gold

## Historical pool

- Discovered: 154713
- Ever alive: 28980
- Ever gold: 1118

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
