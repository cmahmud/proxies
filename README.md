# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 394
- HTTP: 214 alive / 81 gold
- HTTPS: 162 alive / 19 gold
- SOCKS4: 205 alive / 147 gold
- SOCKS5: 219 alive / 147 gold

## Historical pool

- Discovered: 148344
- Ever alive: 26412
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
