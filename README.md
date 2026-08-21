# SyndProxy private pool

## Current pool

- Alive now: 965
- Gold now: 409
- HTTP: 316 alive / 89 gold
- HTTPS: 204 alive / 31 gold
- SOCKS4: 192 alive / 131 gold
- SOCKS5: 253 alive / 158 gold

## Historical pool

- Discovered: 153751
- Ever alive: 28874
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
