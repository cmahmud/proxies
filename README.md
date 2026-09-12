# SyndProxy validated proxy pool

## Current pool

- Alive now: 433
- Gold now: 353
- HTTP: 92 alive / 67 gold
- HTTPS: 33 alive / 17 gold
- SOCKS4: 147 alive / 124 gold
- SOCKS5: 161 alive / 145 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49553
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
