# SyndProxy validated proxy pool

## Current pool

- Alive now: 576
- Gold now: 350
- HTTP: 160 alive / 40 gold
- HTTPS: 68 alive / 10 gold
- SOCKS4: 166 alive / 153 gold
- SOCKS5: 182 alive / 147 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32846
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
