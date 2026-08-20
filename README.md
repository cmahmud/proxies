# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 360
- HTTP: 196 alive / 82 gold
- HTTPS: 136 alive / 18 gold
- SOCKS4: 199 alive / 134 gold
- SOCKS5: 205 alive / 126 gold

## Historical pool

- Discovered: 149496
- Ever alive: 26594
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
