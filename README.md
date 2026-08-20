# SyndProxy private pool

## Current pool

- Alive now: 742
- Gold now: 377
- HTTP: 171 alive / 69 gold
- HTTPS: 153 alive / 17 gold
- SOCKS4: 217 alive / 149 gold
- SOCKS5: 201 alive / 142 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26391
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
