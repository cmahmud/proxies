# SyndProxy private pool

## Current pool

- Alive now: 1167
- Gold now: 476
- HTTP: 433 alive / 123 gold
- HTTPS: 271 alive / 71 gold
- SOCKS4: 235 alive / 141 gold
- SOCKS5: 228 alive / 141 gold

## Historical pool

- Discovered: 113536
- Ever alive: 16536
- Ever gold: 621

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
