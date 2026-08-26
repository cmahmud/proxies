# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 400
- HTTP: 92 alive / 59 gold
- HTTPS: 71 alive / 14 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 175 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39067
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
