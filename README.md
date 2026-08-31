# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 413
- HTTP: 99 alive / 58 gold
- HTTPS: 64 alive / 26 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45505
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
