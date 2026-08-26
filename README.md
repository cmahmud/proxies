# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 410
- HTTP: 99 alive / 64 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39008
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
