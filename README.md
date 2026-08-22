# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 376
- HTTP: 258 alive / 84 gold
- HTTPS: 147 alive / 23 gold
- SOCKS4: 204 alive / 114 gold
- SOCKS5: 243 alive / 155 gold

## Historical pool

- Discovered: 166338
- Ever alive: 32401
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
