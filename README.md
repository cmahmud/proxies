# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 402
- HTTP: 97 alive / 62 gold
- HTTPS: 87 alive / 15 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39271
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
