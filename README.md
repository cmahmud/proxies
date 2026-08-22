# SyndProxy private pool

## Current pool

- Alive now: 818
- Gold now: 391
- HTTP: 214 alive / 97 gold
- HTTPS: 211 alive / 23 gold
- SOCKS4: 184 alive / 127 gold
- SOCKS5: 209 alive / 144 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31362
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
