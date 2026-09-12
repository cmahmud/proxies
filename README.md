# SyndProxy validated proxy pool

## Current pool

- Alive now: 398
- Gold now: 322
- HTTP: 83 alive / 66 gold
- HTTPS: 46 alive / 20 gold
- SOCKS4: 117 alive / 105 gold
- SOCKS5: 152 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49492
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
