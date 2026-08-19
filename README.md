# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 543
- HTTP: 352 alive / 165 gold
- HTTPS: 288 alive / 91 gold
- SOCKS4: 218 alive / 141 gold
- SOCKS5: 226 alive / 146 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18575
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
