# SyndProxy validated proxy pool

## Current pool

- Alive now: 584
- Gold now: 427
- HTTP: 107 alive / 68 gold
- HTTPS: 92 alive / 23 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 201 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35979
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
