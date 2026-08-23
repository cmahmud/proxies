# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 345
- HTTP: 124 alive / 38 gold
- HTTPS: 112 alive / 8 gold
- SOCKS4: 181 alive / 154 gold
- SOCKS5: 212 alive / 145 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32878
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
