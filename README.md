# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 437
- HTTP: 97 alive / 77 gold
- HTTPS: 94 alive / 24 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 187 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47594
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
