# SyndProxy private pool

## Current pool

- Alive now: 1097
- Gold now: 417
- HTTP: 429 alive / 94 gold
- HTTPS: 214 alive / 30 gold
- SOCKS4: 217 alive / 133 gold
- SOCKS5: 237 alive / 160 gold

## Historical pool

- Discovered: 162974
- Ever alive: 31678
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
