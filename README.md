# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 394
- HTTP: 106 alive / 55 gold
- HTTPS: 53 alive / 15 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 203 alive / 164 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33530
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
