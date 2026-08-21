# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 411
- HTTP: 231 alive / 92 gold
- HTTPS: 164 alive / 23 gold
- SOCKS4: 200 alive / 140 gold
- SOCKS5: 239 alive / 156 gold

## Historical pool

- Discovered: 154719
- Ever alive: 29068
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
