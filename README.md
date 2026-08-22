# SyndProxy private pool

## Current pool

- Alive now: 879
- Gold now: 384
- HTTP: 279 alive / 89 gold
- HTTPS: 155 alive / 20 gold
- SOCKS4: 184 alive / 117 gold
- SOCKS5: 261 alive / 158 gold

## Historical pool

- Discovered: 166329
- Ever alive: 32394
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
