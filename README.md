# SyndProxy private pool

## Current pool

- Alive now: 887
- Gold now: 279
- HTTP: 276 alive / 28 gold
- HTTPS: 162 alive / 5 gold
- SOCKS4: 239 alive / 137 gold
- SOCKS5: 210 alive / 109 gold

## Historical pool

- Discovered: 99957
- Ever alive: 12384
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
