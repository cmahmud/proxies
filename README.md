# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 384
- HTTP: 124 alive / 64 gold
- HTTPS: 56 alive / 11 gold
- SOCKS4: 176 alive / 152 gold
- SOCKS5: 198 alive / 157 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
