# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 394
- HTTP: 394 alive / 86 gold
- HTTPS: 201 alive / 20 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 229 alive / 147 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29743
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
