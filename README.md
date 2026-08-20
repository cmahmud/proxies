# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 413
- HTTP: 372 alive / 99 gold
- HTTPS: 253 alive / 22 gold
- SOCKS4: 194 alive / 128 gold
- SOCKS5: 320 alive / 164 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24870
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
