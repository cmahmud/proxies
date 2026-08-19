# SyndProxy private pool

## Current pool

- Alive now: 1161
- Gold now: 548
- HTTP: 391 alive / 172 gold
- HTTPS: 320 alive / 79 gold
- SOCKS4: 228 alive / 149 gold
- SOCKS5: 222 alive / 148 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19761
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
