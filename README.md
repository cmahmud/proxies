# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 394
- HTTP: 191 alive / 69 gold
- HTTPS: 106 alive / 22 gold
- SOCKS4: 165 alive / 149 gold
- SOCKS5: 212 alive / 154 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39452
- Ever gold: 1298

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
