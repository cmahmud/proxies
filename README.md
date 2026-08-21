# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 393
- HTTP: 178 alive / 86 gold
- HTTPS: 113 alive / 19 gold
- SOCKS4: 222 alive / 136 gold
- SOCKS5: 231 alive / 152 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29760
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
