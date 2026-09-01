# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 462
- HTTP: 128 alive / 87 gold
- HTTPS: 128 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 193 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46806
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
