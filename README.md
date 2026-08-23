# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 393
- HTTP: 105 alive / 66 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 163 alive / 151 gold
- SOCKS5: 186 alive / 161 gold

## Historical pool

- Discovered: 175447
- Ever alive: 33162
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
