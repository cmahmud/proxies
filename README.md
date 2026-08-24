# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 408
- HTTP: 113 alive / 71 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 183 alive / 163 gold

## Historical pool

- Discovered: 177314
- Ever alive: 33276
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
