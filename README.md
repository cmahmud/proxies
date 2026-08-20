# SyndProxy private pool

## Current pool

- Alive now: 652
- Gold now: 388
- HTTP: 155 alive / 65 gold
- HTTPS: 81 alive / 17 gold
- SOCKS4: 208 alive / 152 gold
- SOCKS5: 208 alive / 154 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25718
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
