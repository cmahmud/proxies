# SyndProxy private pool

## Current pool

- Alive now: 719
- Gold now: 377
- HTTP: 155 alive / 65 gold
- HTTPS: 140 alive / 19 gold
- SOCKS4: 216 alive / 148 gold
- SOCKS5: 208 alive / 145 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26374
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
