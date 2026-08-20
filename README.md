# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 362
- HTTP: 269 alive / 81 gold
- HTTPS: 220 alive / 21 gold
- SOCKS4: 198 alive / 134 gold
- SOCKS5: 196 alive / 126 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26581
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
