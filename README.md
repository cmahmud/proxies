# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 412
- HTTP: 90 alive / 68 gold
- HTTPS: 88 alive / 18 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 187 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42681
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
