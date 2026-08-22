# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 410
- HTTP: 282 alive / 84 gold
- HTTPS: 167 alive / 28 gold
- SOCKS4: 245 alive / 152 gold
- SOCKS5: 230 alive / 146 gold

## Historical pool

- Discovered: 166318
- Ever alive: 32383
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
