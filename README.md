# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 444
- HTTP: 105 alive / 82 gold
- HTTPS: 105 alive / 26 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47558
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
