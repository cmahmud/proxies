# SyndProxy validated proxy pool

## Current pool

- Alive now: 599
- Gold now: 444
- HTTP: 129 alive / 79 gold
- HTTPS: 97 alive / 32 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 206 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45386
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
