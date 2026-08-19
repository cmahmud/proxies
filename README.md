# SyndProxy private pool

## Current pool

- Alive now: 1030
- Gold now: 484
- HTTP: 350 alive / 126 gold
- HTTPS: 256 alive / 82 gold
- SOCKS4: 191 alive / 122 gold
- SOCKS5: 233 alive / 154 gold

## Historical pool

- Discovered: 119650
- Ever alive: 17862
- Ever gold: 693

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
