# SyndProxy private pool

## Current pool

- Alive now: 1258
- Gold now: 552
- HTTP: 448 alive / 173 gold
- HTTPS: 370 alive / 84 gold
- SOCKS4: 229 alive / 147 gold
- SOCKS5: 211 alive / 148 gold

## Historical pool

- Discovered: 127339
- Ever alive: 19757
- Ever gold: 777

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
