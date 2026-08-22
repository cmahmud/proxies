# SyndProxy private pool

## Current pool

- Alive now: 814
- Gold now: 390
- HTTP: 215 alive / 82 gold
- HTTPS: 172 alive / 26 gold
- SOCKS4: 215 alive / 146 gold
- SOCKS5: 212 alive / 136 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31867
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
