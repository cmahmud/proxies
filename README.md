# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 349
- HTTP: 374 alive / 68 gold
- HTTPS: 271 alive / 17 gold
- SOCKS4: 202 alive / 109 gold
- SOCKS5: 237 alive / 155 gold

## Historical pool

- Discovered: 112040
- Ever alive: 16338
- Ever gold: 508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
