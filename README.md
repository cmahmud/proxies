# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 394
- HTTP: 118 alive / 74 gold
- HTTPS: 37 alive / 13 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33276
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
