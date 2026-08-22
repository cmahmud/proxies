# SyndProxy private pool

## Current pool

- Alive now: 782
- Gold now: 385
- HTTP: 217 alive / 85 gold
- HTTPS: 158 alive / 24 gold
- SOCKS4: 196 alive / 128 gold
- SOCKS5: 211 alive / 148 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31338
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
