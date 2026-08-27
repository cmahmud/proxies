# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 422
- HTTP: 99 alive / 75 gold
- HTTPS: 101 alive / 25 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 173 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41785
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
