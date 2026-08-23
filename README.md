# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 342
- HTTP: 112 alive / 38 gold
- HTTPS: 78 alive / 11 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 182 alive / 142 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32823
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
