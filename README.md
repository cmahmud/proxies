# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 479
- HTTP: 146 alive / 100 gold
- HTTPS: 127 alive / 42 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45031
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
