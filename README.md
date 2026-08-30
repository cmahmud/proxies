# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 446
- HTTP: 109 alive / 82 gold
- HTTPS: 44 alive / 29 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 182 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43684
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
