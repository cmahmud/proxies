# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 403
- HTTP: 112 alive / 61 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 185 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38729
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
