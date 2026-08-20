# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 361
- HTTP: 203 alive / 80 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 204 alive / 134 gold
- SOCKS5: 205 alive / 127 gold

## Historical pool

- Discovered: 149496
- Ever alive: 26594
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
