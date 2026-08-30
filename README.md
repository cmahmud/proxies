# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 425
- HTTP: 136 alive / 82 gold
- HTTPS: 70 alive / 32 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 263 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43899
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
