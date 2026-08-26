# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 421
- HTTP: 90 alive / 68 gold
- HTTPS: 84 alive / 22 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37967
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
