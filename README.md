# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 373
- HTTP: 191 alive / 78 gold
- HTTPS: 202 alive / 20 gold
- SOCKS4: 192 alive / 135 gold
- SOCKS5: 195 alive / 140 gold

## Historical pool

- Discovered: 148840
- Ever alive: 26518
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
