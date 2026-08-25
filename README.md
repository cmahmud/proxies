# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 424
- HTTP: 110 alive / 68 gold
- HTTPS: 108 alive / 24 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35545
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
