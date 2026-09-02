# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 445
- HTTP: 144 alive / 77 gold
- HTTPS: 118 alive / 29 gold
- SOCKS4: 183 alive / 165 gold
- SOCKS5: 187 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47623
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
