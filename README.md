# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 398
- HTTP: 114 alive / 74 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 165 alive / 156 gold
- SOCKS5: 189 alive / 154 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33275
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
