# SyndProxy private pool

## Current pool

- Alive now: 754
- Gold now: 378
- HTTP: 192 alive / 73 gold
- HTTPS: 146 alive / 15 gold
- SOCKS4: 209 alive / 148 gold
- SOCKS5: 207 alive / 142 gold

## Historical pool

- Discovered: 148341
- Ever alive: 26400
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
