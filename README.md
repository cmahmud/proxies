# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 443
- HTTP: 134 alive / 80 gold
- HTTPS: 118 alive / 25 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47650
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
