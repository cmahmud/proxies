# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 406
- HTTP: 264 alive / 89 gold
- HTTPS: 224 alive / 23 gold
- SOCKS4: 217 alive / 128 gold
- SOCKS5: 270 alive / 166 gold

## Historical pool

- Discovered: 164910
- Ever alive: 32130
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
