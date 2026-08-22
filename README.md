# SyndProxy private pool

## Current pool

- Alive now: 1107
- Gold now: 377
- HTTP: 415 alive / 87 gold
- HTTPS: 272 alive / 25 gold
- SOCKS4: 167 alive / 102 gold
- SOCKS5: 253 alive / 163 gold

## Historical pool

- Discovered: 166626
- Ever alive: 32460
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
