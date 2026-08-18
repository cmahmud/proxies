# SyndProxy private pool

## Current pool

- Alive now: 945
- Gold now: 308
- HTTP: 289 alive / 40 gold
- HTTPS: 198 alive / 10 gold
- SOCKS4: 237 alive / 130 gold
- SOCKS5: 221 alive / 128 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14260
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
