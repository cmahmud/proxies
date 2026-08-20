# SyndProxy private pool

## Current pool

- Alive now: 733
- Gold now: 379
- HTTP: 158 alive / 68 gold
- HTTPS: 150 alive / 20 gold
- SOCKS4: 219 alive / 149 gold
- SOCKS5: 206 alive / 142 gold

## Historical pool

- Discovered: 148340
- Ever alive: 26383
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
