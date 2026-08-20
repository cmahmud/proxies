# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 360
- HTTP: 256 alive / 78 gold
- HTTPS: 205 alive / 21 gold
- SOCKS4: 197 alive / 134 gold
- SOCKS5: 192 alive / 127 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26574
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
