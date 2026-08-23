# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 342
- HTTP: 127 alive / 38 gold
- HTTPS: 68 alive / 10 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 181 alive / 142 gold

## Historical pool

- Discovered: 171039
- Ever alive: 32825
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
