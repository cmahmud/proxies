# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 398
- HTTP: 115 alive / 67 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33281
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
