# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 405
- HTTP: 93 alive / 62 gold
- HTTPS: 70 alive / 19 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38528
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
