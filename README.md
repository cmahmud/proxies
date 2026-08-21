# SyndProxy private pool

## Current pool

- Alive now: 790
- Gold now: 381
- HTTP: 237 alive / 77 gold
- HTTPS: 122 alive / 19 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 220 alive / 149 gold

## Historical pool

- Discovered: 157559
- Ever alive: 29766
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
