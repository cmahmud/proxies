# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 437
- HTTP: 125 alive / 82 gold
- HTTPS: 71 alive / 29 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44300
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
