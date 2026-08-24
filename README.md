# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 418
- HTTP: 149 alive / 73 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33845
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
