# SyndProxy private pool

## Current pool

- Alive now: 717
- Gold now: 309
- HTTP: 243 alive / 71 gold
- HTTPS: 109 alive / 21 gold
- SOCKS4: 183 alive / 105 gold
- SOCKS5: 182 alive / 112 gold

## Historical pool

- Discovered: 157559
- Ever alive: 29766
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
