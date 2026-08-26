# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 412
- HTTP: 103 alive / 66 gold
- HTTPS: 97 alive / 19 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38058
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
