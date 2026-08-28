# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 410
- HTTP: 93 alive / 68 gold
- HTTPS: 94 alive / 19 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 186 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42647
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
