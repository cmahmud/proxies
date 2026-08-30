# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 452
- HTTP: 105 alive / 84 gold
- HTTPS: 46 alive / 30 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43683
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
