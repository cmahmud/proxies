# SyndProxy private pool

## Current pool

- Alive now: 824
- Gold now: 356
- HTTP: 279 alive / 86 gold
- HTTPS: 146 alive / 21 gold
- SOCKS4: 192 alive / 119 gold
- SOCKS5: 207 alive / 130 gold

## Historical pool

- Discovered: 167412
- Ever alive: 32584
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
