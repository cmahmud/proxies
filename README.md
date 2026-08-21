# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 394
- HTTP: 349 alive / 101 gold
- HTTPS: 243 alive / 32 gold
- SOCKS4: 192 alive / 121 gold
- SOCKS5: 258 alive / 140 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28055
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
