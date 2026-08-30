# SyndProxy validated proxy pool

## Current pool

- Alive now: 661
- Gold now: 485
- HTTP: 163 alive / 101 gold
- HTTPS: 131 alive / 43 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 196 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44991
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
