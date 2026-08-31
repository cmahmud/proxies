# SyndProxy validated proxy pool

## Current pool

- Alive now: 639
- Gold now: 484
- HTTP: 146 alive / 101 gold
- HTTPS: 126 alive / 46 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 194 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45029
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
