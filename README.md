# SyndProxy validated proxy pool

## Current pool

- Alive now: 564
- Gold now: 448
- HTTP: 96 alive / 78 gold
- HTTPS: 98 alive / 32 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 192 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47392
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
