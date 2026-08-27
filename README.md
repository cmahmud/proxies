# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 422
- HTTP: 97 alive / 77 gold
- HTTPS: 71 alive / 22 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 177 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41765
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
