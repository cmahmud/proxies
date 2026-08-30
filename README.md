# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 445
- HTTP: 135 alive / 86 gold
- HTTPS: 78 alive / 34 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 208 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44228
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
