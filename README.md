# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 380
- HTTP: 246 alive / 72 gold
- HTTPS: 120 alive / 21 gold
- SOCKS4: 212 alive / 138 gold
- SOCKS5: 216 alive / 149 gold

## Historical pool

- Discovered: 157559
- Ever alive: 29766
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
