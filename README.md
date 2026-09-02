# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 438
- HTTP: 120 alive / 76 gold
- HTTPS: 119 alive / 24 gold
- SOCKS4: 186 alive / 163 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47606
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
