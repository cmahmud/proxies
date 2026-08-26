# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 420
- HTTP: 90 alive / 70 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37966
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
