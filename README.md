# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 340
- HTTP: 284 alive / 54 gold
- HTTPS: 186 alive / 13 gold
- SOCKS4: 231 alive / 139 gold
- SOCKS5: 223 alive / 134 gold

## Historical pool

- Discovered: 107138
- Ever alive: 14975
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
