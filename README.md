# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 390
- HTTP: 230 alive / 77 gold
- HTTPS: 180 alive / 16 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 216 alive / 148 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26488
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
