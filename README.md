# SyndProxy validated proxy pool

## Current pool

- Alive now: 332
- Gold now: 206
- HTTP: 104 alive / 46 gold
- HTTPS: 34 alive / 6 gold
- SOCKS4: 86 alive / 66 gold
- SOCKS5: 108 alive / 88 gold

## Historical pool

- Discovered: 170533
- Ever alive: 32760
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
