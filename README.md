# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 395
- HTTP: 122 alive / 62 gold
- HTTPS: 48 alive / 10 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33326
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
