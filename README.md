# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 415
- HTTP: 107 alive / 68 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 195 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38028
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
