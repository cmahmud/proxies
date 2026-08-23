# SyndProxy validated proxy pool

## Current pool

- Alive now: 444
- Gold now: 358
- HTTP: 73 alive / 39 gold
- HTTPS: 26 alive / 8 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 180 alive / 157 gold

## Historical pool

- Discovered: 173056
- Ever alive: 33004
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
