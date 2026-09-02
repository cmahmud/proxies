# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 437
- HTTP: 101 alive / 78 gold
- HTTPS: 87 alive / 26 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47678
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
