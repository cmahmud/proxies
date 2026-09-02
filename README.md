# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 438
- HTTP: 106 alive / 76 gold
- HTTPS: 111 alive / 24 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 193 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47603
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
