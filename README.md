# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 542
- HTTP: 358 alive / 165 gold
- HTTPS: 274 alive / 90 gold
- SOCKS4: 215 alive / 141 gold
- SOCKS5: 228 alive / 146 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18575
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
