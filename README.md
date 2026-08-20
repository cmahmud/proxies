# SyndProxy private pool

## Current pool

- Alive now: 1514
- Gold now: 581
- HTTP: 577 alive / 178 gold
- HTTPS: 419 alive / 93 gold
- SOCKS4: 244 alive / 142 gold
- SOCKS5: 274 alive / 168 gold

## Historical pool

- Discovered: 138940
- Ever alive: 23175
- Ever gold: 915

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
