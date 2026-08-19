# SyndProxy private pool

## Current pool

- Alive now: 1131
- Gold now: 540
- HTTP: 415 alive / 157 gold
- HTTPS: 279 alive / 89 gold
- SOCKS4: 230 alive / 160 gold
- SOCKS5: 207 alive / 134 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18228
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
