# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 426
- HTTP: 102 alive / 66 gold
- HTTPS: 90 alive / 27 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 183874
- Ever alive: 35688
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
