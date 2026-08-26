# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 400
- HTTP: 92 alive / 58 gold
- HTTPS: 75 alive / 19 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 185 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38517
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
