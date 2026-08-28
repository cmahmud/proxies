# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 409
- HTTP: 87 alive / 66 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42642
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
