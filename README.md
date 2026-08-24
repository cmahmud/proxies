# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 390
- HTTP: 120 alive / 71 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33249
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
