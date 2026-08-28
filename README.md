# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 402
- HTTP: 78 alive / 59 gold
- HTTPS: 41 alive / 16 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42847
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
