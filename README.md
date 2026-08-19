# SyndProxy private pool

## Current pool

- Alive now: 1179
- Gold now: 521
- HTTP: 424 alive / 170 gold
- HTTPS: 328 alive / 57 gold
- SOCKS4: 223 alive / 148 gold
- SOCKS5: 204 alive / 146 gold

## Historical pool

- Discovered: 127332
- Ever alive: 19729
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
