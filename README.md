# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 420
- HTTP: 150 alive / 74 gold
- HTTPS: 84 alive / 19 gold
- SOCKS4: 183 alive / 159 gold
- SOCKS5: 195 alive / 168 gold

## Historical pool

- Discovered: 181482
- Ever alive: 33845
- Ever gold: 1252

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
