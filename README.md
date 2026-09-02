# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 452
- HTTP: 103 alive / 82 gold
- HTTPS: 98 alive / 31 gold
- SOCKS4: 182 alive / 161 gold
- SOCKS5: 188 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47545
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
