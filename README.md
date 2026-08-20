# SyndProxy private pool

## Current pool

- Alive now: 716
- Gold now: 360
- HTTP: 177 alive / 81 gold
- HTTPS: 142 alive / 20 gold
- SOCKS4: 197 alive / 134 gold
- SOCKS5: 200 alive / 125 gold

## Historical pool

- Discovered: 149496
- Ever alive: 26586
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
