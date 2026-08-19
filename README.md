# SyndProxy private pool

## Current pool

- Alive now: 1150
- Gold now: 512
- HTTP: 392 alive / 172 gold
- HTTPS: 313 alive / 86 gold
- SOCKS4: 228 alive / 128 gold
- SOCKS5: 217 alive / 126 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19764
- Ever gold: 778

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
