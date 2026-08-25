# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 415
- HTTP: 92 alive / 66 gold
- HTTPS: 73 alive / 22 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37045
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
