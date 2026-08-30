# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 483
- HTTP: 155 alive / 103 gold
- HTTPS: 114 alive / 43 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 201 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44975
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
