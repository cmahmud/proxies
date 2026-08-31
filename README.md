# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 436
- HTTP: 138 alive / 72 gold
- HTTPS: 104 alive / 30 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 209 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45396
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
