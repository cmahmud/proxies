# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 424
- HTTP: 101 alive / 77 gold
- HTTPS: 58 alive / 21 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44531
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
