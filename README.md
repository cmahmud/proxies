# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 442
- HTTP: 136 alive / 78 gold
- HTTPS: 106 alive / 26 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 188 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47649
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
