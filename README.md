# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 485
- HTTP: 348 alive / 127 gold
- HTTPS: 258 alive / 82 gold
- SOCKS4: 197 alive / 123 gold
- SOCKS5: 237 alive / 153 gold

## Historical pool

- Discovered: 119691
- Ever alive: 17864
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
