# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 345
- HTTP: 111 alive / 40 gold
- HTTPS: 76 alive / 11 gold
- SOCKS4: 156 alive / 153 gold
- SOCKS5: 181 alive / 141 gold

## Historical pool

- Discovered: 171038
- Ever alive: 32814
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
