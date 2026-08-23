# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 392
- HTTP: 112 alive / 66 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 163 alive / 150 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 175447
- Ever alive: 33162
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
