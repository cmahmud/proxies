# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 483
- HTTP: 154 alive / 102 gold
- HTTPS: 121 alive / 43 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 203 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44976
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
