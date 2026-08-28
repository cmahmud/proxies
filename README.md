# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 393
- HTTP: 73 alive / 57 gold
- HTTPS: 78 alive / 16 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 173 alive / 159 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42891
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
