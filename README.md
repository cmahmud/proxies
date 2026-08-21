# SyndProxy private pool

## Current pool

- Alive now: 1157
- Gold now: 399
- HTTP: 427 alive / 96 gold
- HTTPS: 286 alive / 30 gold
- SOCKS4: 230 alive / 152 gold
- SOCKS5: 214 alive / 121 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30318
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
