# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 416
- HTTP: 115 alive / 69 gold
- HTTPS: 75 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35382
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
