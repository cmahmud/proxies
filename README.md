# SyndProxy private pool

## Current pool

- Alive now: 705
- Gold now: 389
- HTTP: 182 alive / 64 gold
- HTTPS: 104 alive / 19 gold
- SOCKS4: 201 alive / 152 gold
- SOCKS5: 218 alive / 154 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25694
- Ever gold: 1071

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
