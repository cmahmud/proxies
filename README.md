# SyndProxy private pool

## Current pool

- Alive now: 1414
- Gold now: 583
- HTTP: 527 alive / 180 gold
- HTTPS: 374 alive / 94 gold
- SOCKS4: 245 alive / 142 gold
- SOCKS5: 268 alive / 167 gold

## Historical pool

- Discovered: 138941
- Ever alive: 23178
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
