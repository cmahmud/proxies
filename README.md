# SyndProxy private pool

## Current pool

- Alive now: 985
- Gold now: 393
- HTTP: 311 alive / 76 gold
- HTTPS: 198 alive / 13 gold
- SOCKS4: 247 alive / 152 gold
- SOCKS5: 229 alive / 152 gold

## Historical pool

- Discovered: 129305
- Ever alive: 20396
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
