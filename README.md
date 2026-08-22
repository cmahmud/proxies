# SyndProxy private pool

## Current pool

- Alive now: 817
- Gold now: 387
- HTTP: 247 alive / 87 gold
- HTTPS: 134 alive / 23 gold
- SOCKS4: 198 alive / 127 gold
- SOCKS5: 238 alive / 150 gold

## Historical pool

- Discovered: 162003
- Ever alive: 31389
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
