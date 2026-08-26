# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 424
- HTTP: 110 alive / 74 gold
- HTTPS: 92 alive / 21 gold
- SOCKS4: 184 alive / 164 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37855
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
