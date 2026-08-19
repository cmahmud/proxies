# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 542
- HTTP: 363 alive / 164 gold
- HTTPS: 277 alive / 91 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 231 alive / 146 gold

## Historical pool

- Discovered: 122378
- Ever alive: 18580
- Ever gold: 720

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
