# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 538
- HTTP: 360 alive / 163 gold
- HTTPS: 275 alive / 90 gold
- SOCKS4: 215 alive / 139 gold
- SOCKS5: 227 alive / 146 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18562
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
