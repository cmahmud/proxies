# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 387
- HTTP: 213 alive / 79 gold
- HTTPS: 243 alive / 24 gold
- SOCKS4: 211 alive / 146 gold
- SOCKS5: 198 alive / 138 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31873
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
