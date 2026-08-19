# SyndProxy private pool

## Current pool

- Alive now: 1185
- Gold now: 405
- HTTP: 389 alive / 92 gold
- HTTPS: 237 alive / 16 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 337 alive / 150 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21202
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
