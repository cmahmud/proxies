# SyndProxy private pool

## Current pool

- Alive now: 1060
- Gold now: 408
- HTTP: 356 alive / 94 gold
- HTTPS: 234 alive / 33 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 242 alive / 135 gold

## Historical pool

- Discovered: 160997
- Ever alive: 30970
- Ever gold: 1152

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
