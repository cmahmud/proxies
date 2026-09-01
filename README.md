# SyndProxy validated proxy pool

## Current pool

- Alive now: 627
- Gold now: 462
- HTTP: 130 alive / 86 gold
- HTTPS: 130 alive / 34 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 197 alive / 181 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46765
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
