# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 426
- HTTP: 100 alive / 75 gold
- HTTPS: 78 alive / 21 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37892
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
