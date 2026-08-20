# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 412
- HTTP: 310 alive / 94 gold
- HTTPS: 236 alive / 27 gold
- SOCKS4: 193 alive / 129 gold
- SOCKS5: 233 alive / 162 gold

## Historical pool

- Discovered: 144219
- Ever alive: 24902
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
