# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 543
- HTTP: 377 alive / 167 gold
- HTTPS: 237 alive / 91 gold
- SOCKS4: 208 alive / 146 gold
- SOCKS5: 209 alive / 139 gold

## Historical pool

- Discovered: 123168
- Ever alive: 18789
- Ever gold: 728

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
