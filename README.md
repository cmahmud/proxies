# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 441
- HTTP: 126 alive / 83 gold
- HTTPS: 104 alive / 25 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47655
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
