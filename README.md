# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 486
- HTTP: 145 alive / 103 gold
- HTTPS: 120 alive / 44 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 206 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44981
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
