# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 429
- HTTP: 349 alive / 102 gold
- HTTPS: 236 alive / 23 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 268 alive / 158 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28122
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
