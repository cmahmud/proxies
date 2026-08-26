# SyndProxy validated proxy pool

## Current pool

- Alive now: 527
- Gold now: 402
- HTTP: 101 alive / 59 gold
- HTTPS: 66 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39056
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
