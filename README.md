# SyndProxy private pool

## Current pool

- Alive now: 1087
- Gold now: 412
- HTTP: 340 alive / 96 gold
- HTTPS: 277 alive / 24 gold
- SOCKS4: 229 alive / 146 gold
- SOCKS5: 241 alive / 146 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28237
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
