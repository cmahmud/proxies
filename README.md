# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 406
- HTTP: 107 alive / 62 gold
- HTTPS: 162 alive / 14 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40762
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
