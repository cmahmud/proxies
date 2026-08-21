# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 382
- HTTP: 276 alive / 72 gold
- HTTPS: 203 alive / 22 gold
- SOCKS4: 228 alive / 142 gold
- SOCKS5: 230 alive / 146 gold

## Historical pool

- Discovered: 156741
- Ever alive: 29577
- Ever gold: 1132

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
