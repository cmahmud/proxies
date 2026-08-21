# SyndProxy private pool

## Current pool

- Alive now: 844
- Gold now: 379
- HTTP: 264 alive / 92 gold
- HTTPS: 175 alive / 26 gold
- SOCKS4: 196 alive / 148 gold
- SOCKS5: 209 alive / 113 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28933
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
