# SyndProxy validated proxy pool

## Current pool

- Alive now: 480
- Gold now: 401
- HTTP: 78 alive / 59 gold
- HTTPS: 53 alive / 20 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 181 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42830
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
