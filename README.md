# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 400
- HTTP: 84 alive / 54 gold
- HTTPS: 71 alive / 19 gold
- SOCKS4: 174 alive / 165 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41604
- Ever gold: 1341

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
