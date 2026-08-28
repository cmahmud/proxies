# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 409
- HTTP: 96 alive / 65 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 186 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42676
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
