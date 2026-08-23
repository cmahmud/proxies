# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 351
- HTTP: 120 alive / 40 gold
- HTTPS: 60 alive / 9 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 178 alive / 149 gold

## Historical pool

- Discovered: 171048
- Ever alive: 32852
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
