# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 439
- HTTP: 126 alive / 87 gold
- HTTPS: 62 alive / 26 gold
- SOCKS4: 165 alive / 157 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43663
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
