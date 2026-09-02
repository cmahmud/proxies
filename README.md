# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 443
- HTTP: 136 alive / 77 gold
- HTTPS: 115 alive / 27 gold
- SOCKS4: 186 alive / 165 gold
- SOCKS5: 185 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47627
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
