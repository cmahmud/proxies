# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 446
- HTTP: 130 alive / 79 gold
- HTTPS: 105 alive / 29 gold
- SOCKS4: 186 alive / 165 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47634
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
