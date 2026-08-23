# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 393
- HTTP: 108 alive / 66 gold
- HTTPS: 57 alive / 15 gold
- SOCKS4: 175 alive / 153 gold
- SOCKS5: 195 alive / 159 gold

## Historical pool

- Discovered: 175447
- Ever alive: 33160
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
