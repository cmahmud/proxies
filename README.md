# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 416
- HTTP: 111 alive / 69 gold
- HTTPS: 152 alive / 18 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41222
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
