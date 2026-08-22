# SyndProxy private pool

## Current pool

- Alive now: 780
- Gold now: 392
- HTTP: 207 alive / 83 gold
- HTTPS: 157 alive / 23 gold
- SOCKS4: 205 alive / 148 gold
- SOCKS5: 211 alive / 138 gold

## Historical pool

- Discovered: 163332
- Ever alive: 31878
- Ever gold: 1168

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
