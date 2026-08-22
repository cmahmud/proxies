# SyndProxy private pool

## Current pool

- Alive now: 838
- Gold now: 389
- HTTP: 232 alive / 83 gold
- HTTPS: 177 alive / 23 gold
- SOCKS4: 209 alive / 145 gold
- SOCKS5: 220 alive / 138 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31882
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
