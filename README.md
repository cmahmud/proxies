# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 257
- HTTP: 253 alive / 28 gold
- HTTPS: 160 alive / 4 gold
- SOCKS4: 218 alive / 117 gold
- SOCKS5: 218 alive / 108 gold

## Historical pool

- Discovered: 99107
- Ever alive: 11821
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
