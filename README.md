# SyndProxy private pool

## Current pool

- Alive now: 867
- Gold now: 352
- HTTP: 261 alive / 75 gold
- HTTPS: 218 alive / 18 gold
- SOCKS4: 198 alive / 132 gold
- SOCKS5: 190 alive / 127 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26568
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
