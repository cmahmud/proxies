# SyndProxy validated proxy pool

## Current pool

- Alive now: 444
- Gold now: 359
- HTTP: 100 alive / 70 gold
- HTTPS: 51 alive / 23 gold
- SOCKS4: 109 alive / 96 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48710
- Ever gold: 1564

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
