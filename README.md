# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 466
- HTTP: 125 alive / 92 gold
- HTTPS: 120 alive / 37 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 203 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44896
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
