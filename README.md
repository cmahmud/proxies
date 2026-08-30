# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 417
- HTTP: 119 alive / 83 gold
- HTTPS: 65 alive / 26 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43696
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
