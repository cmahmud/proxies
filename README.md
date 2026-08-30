# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 447
- HTTP: 113 alive / 84 gold
- HTTPS: 53 alive / 28 gold
- SOCKS4: 172 alive / 164 gold
- SOCKS5: 181 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43691
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
