# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 227
- HTTP: 140 alive / 37 gold
- HTTPS: 72 alive / 5 gold
- SOCKS4: 166 alive / 86 gold
- SOCKS5: 182 alive / 99 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32785
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
