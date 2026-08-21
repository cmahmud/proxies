# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 380
- HTTP: 295 alive / 89 gold
- HTTPS: 224 alive / 30 gold
- SOCKS4: 176 alive / 123 gold
- SOCKS5: 221 alive / 138 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28863
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
