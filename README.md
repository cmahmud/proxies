# SyndProxy validated proxy pool

## Current pool

- Alive now: 607
- Gold now: 458
- HTTP: 125 alive / 83 gold
- HTTPS: 127 alive / 36 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 187 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46794
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
