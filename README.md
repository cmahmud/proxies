# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 306
- HTTP: 121 alive / 37 gold
- HTTPS: 58 alive / 10 gold
- SOCKS4: 195 alive / 152 gold
- SOCKS5: 182 alive / 107 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32825
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
