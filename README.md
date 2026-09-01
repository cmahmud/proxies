# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 457
- HTTP: 137 alive / 85 gold
- HTTPS: 130 alive / 36 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46830
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
