# SyndProxy private pool

## Current pool

- Alive now: 922
- Gold now: 369
- HTTP: 297 alive / 83 gold
- HTTPS: 198 alive / 21 gold
- SOCKS4: 206 alive / 126 gold
- SOCKS5: 221 alive / 139 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29817
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
