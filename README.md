# SyndProxy private pool

## Current pool

- Alive now: 1377
- Gold now: 551
- HTTP: 442 alive / 184 gold
- HTTPS: 352 alive / 89 gold
- SOCKS4: 233 alive / 148 gold
- SOCKS5: 350 alive / 130 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23617
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
