# SyndProxy private pool

## Current pool

- Alive now: 1193
- Gold now: 443
- HTTP: 396 alive / 109 gold
- HTTPS: 327 alive / 32 gold
- SOCKS4: 215 alive / 152 gold
- SOCKS5: 255 alive / 150 gold

## Historical pool

- Discovered: 153725
- Ever alive: 28560
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
