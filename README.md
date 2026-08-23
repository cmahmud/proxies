# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 353
- HTTP: 91 alive / 35 gold
- HTTPS: 53 alive / 10 gold
- SOCKS4: 178 alive / 152 gold
- SOCKS5: 203 alive / 156 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32957
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
