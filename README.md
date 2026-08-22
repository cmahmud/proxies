# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 398
- HTTP: 300 alive / 90 gold
- HTTPS: 237 alive / 23 gold
- SOCKS4: 220 alive / 135 gold
- SOCKS5: 228 alive / 150 gold

## Historical pool

- Discovered: 164246
- Ever alive: 32085
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
