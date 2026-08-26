# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 411
- HTTP: 101 alive / 65 gold
- HTTPS: 98 alive / 18 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38041
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
