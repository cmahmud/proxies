# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 411
- HTTP: 85 alive / 64 gold
- HTTPS: 83 alive / 20 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 190 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38623
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
