# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 439
- HTTP: 134 alive / 76 gold
- HTTPS: 126 alive / 26 gold
- SOCKS4: 187 alive / 163 gold
- SOCKS5: 186 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47619
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
