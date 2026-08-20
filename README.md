# SyndProxy private pool

## Current pool

- Alive now: 652
- Gold now: 350
- HTTP: 170 alive / 66 gold
- HTTPS: 111 alive / 21 gold
- SOCKS4: 177 alive / 124 gold
- SOCKS5: 194 alive / 139 gold

## Historical pool

- Discovered: 145580
- Ever alive: 25581
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
