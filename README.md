# SyndProxy validated proxy pool

## Current pool

- Alive now: 666
- Gold now: 483
- HTTP: 158 alive / 100 gold
- HTTPS: 141 alive / 45 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 198 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44967
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
