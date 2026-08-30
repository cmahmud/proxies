# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 471
- HTTP: 132 alive / 94 gold
- HTTPS: 111 alive / 43 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 203 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44910
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
