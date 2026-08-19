# SyndProxy private pool

## Current pool

- Alive now: 980
- Gold now: 397
- HTTP: 284 alive / 72 gold
- HTTPS: 226 alive / 16 gold
- SOCKS4: 242 alive / 149 gold
- SOCKS5: 228 alive / 160 gold

## Historical pool

- Discovered: 129319
- Ever alive: 20485
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
