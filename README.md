# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 397
- HTTP: 126 alive / 61 gold
- HTTPS: 71 alive / 14 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33508
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
