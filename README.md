# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 424
- HTTP: 108 alive / 79 gold
- HTTPS: 54 alive / 20 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44514
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
