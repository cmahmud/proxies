# SyndProxy private pool

## Current pool

- Alive now: 1004
- Gold now: 429
- HTTP: 322 alive / 86 gold
- HTTPS: 181 alive / 28 gold
- SOCKS4: 227 alive / 155 gold
- SOCKS5: 274 alive / 160 gold

## Historical pool

- Discovered: 164933
- Ever alive: 32185
- Ever gold: 1173

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
