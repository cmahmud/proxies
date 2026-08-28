# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 419
- HTTP: 95 alive / 72 gold
- HTTPS: 95 alive / 23 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42618
- Ever gold: 1359

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
