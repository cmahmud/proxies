# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 399
- HTTP: 92 alive / 58 gold
- HTTPS: 71 alive / 17 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38564
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
