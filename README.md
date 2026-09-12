# SyndProxy validated proxy pool

## Current pool

- Alive now: 396
- Gold now: 322
- HTTP: 86 alive / 66 gold
- HTTPS: 43 alive / 20 gold
- SOCKS4: 116 alive / 105 gold
- SOCKS5: 151 alive / 131 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49491
- Ever gold: 1585

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
