# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 401
- HTTP: 392 alive / 93 gold
- HTTPS: 254 alive / 14 gold
- SOCKS4: 232 alive / 146 gold
- SOCKS5: 299 alive / 148 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21223
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
