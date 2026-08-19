# SyndProxy private pool

## Current pool

- Alive now: 1164
- Gold now: 542
- HTTP: 413 alive / 187 gold
- HTTPS: 313 alive / 78 gold
- SOCKS4: 231 alive / 133 gold
- SOCKS5: 207 alive / 144 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19811
- Ever gold: 798

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
