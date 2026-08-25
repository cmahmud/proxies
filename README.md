# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 394
- HTTP: 96 alive / 64 gold
- HTTPS: 65 alive / 19 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 170 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37500
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
