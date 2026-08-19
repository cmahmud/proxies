# SyndProxy private pool

## Current pool

- Alive now: 1193
- Gold now: 527
- HTTP: 432 alive / 174 gold
- HTTPS: 324 alive / 57 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 212 alive / 147 gold

## Historical pool

- Discovered: 127332
- Ever alive: 19716
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
