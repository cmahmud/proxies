# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 472
- HTTP: 148 alive / 97 gold
- HTTPS: 124 alive / 39 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 200 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46955
- Ever gold: 1461

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
