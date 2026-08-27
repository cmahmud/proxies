# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 422
- HTTP: 100 alive / 75 gold
- HTTPS: 109 alive / 25 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 171 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41787
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
