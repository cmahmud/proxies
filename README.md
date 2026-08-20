# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 354
- HTTP: 258 alive / 75 gold
- HTTPS: 199 alive / 19 gold
- SOCKS4: 198 alive / 133 gold
- SOCKS5: 190 alive / 127 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26572
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
