# SyndProxy validated proxy pool

## Current pool

- Alive now: 642
- Gold now: 485
- HTTP: 143 alive / 101 gold
- HTTPS: 120 alive / 47 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 207 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45012
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
