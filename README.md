# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 430
- HTTP: 116 alive / 79 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44536
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
