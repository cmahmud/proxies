# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 393
- HTTP: 344 alive / 102 gold
- HTTPS: 242 alive / 30 gold
- SOCKS4: 199 alive / 121 gold
- SOCKS5: 257 alive / 140 gold

## Historical pool

- Discovered: 152746
- Ever alive: 28049
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
