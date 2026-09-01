# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 457
- HTTP: 122 alive / 86 gold
- HTTPS: 121 alive / 30 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 191 alive / 181 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46776
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
