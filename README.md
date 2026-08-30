# SyndProxy validated proxy pool

## Current pool

- Alive now: 616
- Gold now: 458
- HTTP: 128 alive / 93 gold
- HTTPS: 119 alive / 36 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44830
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
