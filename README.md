# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 457
- HTTP: 129 alive / 87 gold
- HTTPS: 98 alive / 35 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 210 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45350
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
