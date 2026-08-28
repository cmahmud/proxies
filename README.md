# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 407
- HTTP: 93 alive / 62 gold
- HTTPS: 65 alive / 17 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42739
- Ever gold: 1360

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
