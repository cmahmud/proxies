# SyndProxy private pool

## Current pool

- Alive now: 858
- Gold now: 384
- HTTP: 204 alive / 79 gold
- HTTPS: 245 alive / 22 gold
- SOCKS4: 212 alive / 145 gold
- SOCKS5: 197 alive / 138 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31873
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
