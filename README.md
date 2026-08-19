# SyndProxy private pool

## Current pool

- Alive now: 1026
- Gold now: 353
- HTTP: 321 alive / 68 gold
- HTTPS: 242 alive / 11 gold
- SOCKS4: 233 alive / 126 gold
- SOCKS5: 230 alive / 148 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20270
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
