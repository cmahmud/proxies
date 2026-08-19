# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 508
- HTTP: 342 alive / 143 gold
- HTTPS: 246 alive / 81 gold
- SOCKS4: 234 alive / 149 gold
- SOCKS5: 203 alive / 135 gold

## Historical pool

- Discovered: 119808
- Ever alive: 17940
- Ever gold: 705

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
