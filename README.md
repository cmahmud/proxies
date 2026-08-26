# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 411
- HTTP: 102 alive / 65 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 174 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37811
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
