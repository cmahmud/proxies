# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 386
- HTTP: 107 alive / 54 gold
- HTTPS: 32 alive / 11 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
