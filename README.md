# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 407
- HTTP: 113 alive / 64 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35453
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
