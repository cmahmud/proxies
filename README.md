# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 392
- HTTP: 323 alive / 98 gold
- HTTPS: 224 alive / 21 gold
- SOCKS4: 197 alive / 127 gold
- SOCKS5: 279 alive / 146 gold

## Historical pool

- Discovered: 136236
- Ever alive: 22543
- Ever gold: 908

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
