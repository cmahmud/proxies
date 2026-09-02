# SyndProxy validated proxy pool

## Current pool

- Alive now: 603
- Gold now: 439
- HTTP: 112 alive / 77 gold
- HTTPS: 114 alive / 24 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47604
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
