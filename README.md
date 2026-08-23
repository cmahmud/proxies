# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 240
- HTTP: 134 alive / 37 gold
- HTTPS: 72 alive / 5 gold
- SOCKS4: 166 alive / 88 gold
- SOCKS5: 182 alive / 110 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32785
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
