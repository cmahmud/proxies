# SyndProxy validated proxy pool

## Current pool

- Alive now: 572
- Gold now: 425
- HTTP: 104 alive / 67 gold
- HTTPS: 86 alive / 22 gold
- SOCKS4: 183 alive / 160 gold
- SOCKS5: 199 alive / 176 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35979
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
