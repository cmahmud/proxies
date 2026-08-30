# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 445
- HTTP: 118 alive / 80 gold
- HTTPS: 114 alive / 35 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44644
- Ever gold: 1408

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
