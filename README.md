# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 466
- HTTP: 135 alive / 92 gold
- HTTPS: 112 alive / 40 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 200 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44903
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
