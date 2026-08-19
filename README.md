# SyndProxy private pool

## Current pool

- Alive now: 1207
- Gold now: 403
- HTTP: 396 alive / 86 gold
- HTTPS: 266 alive / 16 gold
- SOCKS4: 238 alive / 148 gold
- SOCKS5: 307 alive / 153 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21980
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
