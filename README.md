# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 423
- HTTP: 112 alive / 75 gold
- HTTPS: 84 alive / 21 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 182 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37870
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
