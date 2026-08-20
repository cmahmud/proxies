# SyndProxy private pool

## Current pool

- Alive now: 1362
- Gold now: 526
- HTTP: 478 alive / 175 gold
- HTTPS: 346 alive / 60 gold
- SOCKS4: 207 alive / 124 gold
- SOCKS5: 331 alive / 167 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24844
- Ever gold: 1050

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
