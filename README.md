# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 477
- HTTP: 136 alive / 101 gold
- HTTPS: 129 alive / 41 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45058
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
