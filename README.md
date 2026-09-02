# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 442
- HTTP: 102 alive / 77 gold
- HTTPS: 99 alive / 28 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47661
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
