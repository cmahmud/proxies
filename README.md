# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 453
- HTTP: 153 alive / 84 gold
- HTTPS: 102 alive / 35 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 209 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45422
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
