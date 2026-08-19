# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 298
- HTTP: 338 alive / 63 gold
- HTTPS: 216 alive / 19 gold
- SOCKS4: 200 alive / 113 gold
- SOCKS5: 207 alive / 103 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15505
- Ever gold: 497

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
