# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 401
- HTTP: 93 alive / 59 gold
- HTTPS: 70 alive / 16 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38455
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
