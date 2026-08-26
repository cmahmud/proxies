# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 410
- HTTP: 110 alive / 66 gold
- HTTPS: 113 alive / 16 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38072
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
