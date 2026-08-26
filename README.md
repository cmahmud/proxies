# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 414
- HTTP: 100 alive / 66 gold
- HTTPS: 71 alive / 21 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 172 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37812
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
