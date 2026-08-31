# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 440
- HTTP: 149 alive / 77 gold
- HTTPS: 99 alive / 30 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 218 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45413
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
