# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 404
- HTTP: 118 alive / 71 gold
- HTTPS: 46 alive / 14 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33276
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
