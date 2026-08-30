# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 450
- HTTP: 115 alive / 89 gold
- HTTPS: 54 alive / 31 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 177 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43676
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
