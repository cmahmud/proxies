# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 439
- HTTP: 107 alive / 79 gold
- HTTPS: 93 alive / 25 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 191 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47659
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
