# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 364
- HTTP: 198 alive / 73 gold
- HTTPS: 209 alive / 16 gold
- SOCKS4: 200 alive / 135 gold
- SOCKS5: 197 alive / 140 gold

## Historical pool

- Discovered: 149285
- Ever alive: 26525
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
