# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 431
- HTTP: 110 alive / 72 gold
- HTTPS: 63 alive / 25 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 192 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45543
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
