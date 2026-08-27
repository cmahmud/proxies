# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 405
- HTTP: 112 alive / 61 gold
- HTTPS: 174 alive / 17 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 175 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40893
- Ever gold: 1313

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
