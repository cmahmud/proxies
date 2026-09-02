# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 441
- HTTP: 142 alive / 77 gold
- HTTPS: 120 alive / 26 gold
- SOCKS4: 191 alive / 165 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47620
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
