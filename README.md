# SyndProxy private pool

## Current pool

- Alive now: 718
- Gold now: 371
- HTTP: 179 alive / 70 gold
- HTTPS: 139 alive / 18 gold
- SOCKS4: 204 alive / 147 gold
- SOCKS5: 196 alive / 136 gold

## Historical pool

- Discovered: 148334
- Ever alive: 26211
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
