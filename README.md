# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 418
- HTTP: 99 alive / 74 gold
- HTTPS: 111 alive / 23 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 173 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41825
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
