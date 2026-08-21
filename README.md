# SyndProxy private pool

## Current pool

- Alive now: 1296
- Gold now: 427
- HTTP: 522 alive / 96 gold
- HTTPS: 331 alive / 29 gold
- SOCKS4: 203 alive / 142 gold
- SOCKS5: 240 alive / 160 gold

## Historical pool

- Discovered: 159271
- Ever alive: 30392
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
