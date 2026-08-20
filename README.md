# SyndProxy private pool

## Current pool

- Alive now: 713
- Gold now: 362
- HTTP: 181 alive / 83 gold
- HTTPS: 140 alive / 20 gold
- SOCKS4: 194 alive / 133 gold
- SOCKS5: 198 alive / 126 gold

## Historical pool

- Discovered: 149496
- Ever alive: 26590
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
