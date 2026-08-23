# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 334
- HTTP: 114 alive / 36 gold
- HTTPS: 60 alive / 10 gold
- SOCKS4: 177 alive / 147 gold
- SOCKS5: 173 alive / 141 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32792
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
