# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 444
- HTTP: 118 alive / 75 gold
- HTTPS: 142 alive / 40 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44674
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
