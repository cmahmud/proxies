# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 385
- HTTP: 240 alive / 73 gold
- HTTPS: 169 alive / 15 gold
- SOCKS4: 211 alive / 148 gold
- SOCKS5: 206 alive / 149 gold

## Historical pool

- Discovered: 148549
- Ever alive: 26468
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
