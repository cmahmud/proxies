# SyndProxy private pool

## Current pool

- Alive now: 1180
- Gold now: 414
- HTTP: 389 alive / 82 gold
- HTTPS: 255 alive / 17 gold
- SOCKS4: 271 alive / 150 gold
- SOCKS5: 265 alive / 165 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20633
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
