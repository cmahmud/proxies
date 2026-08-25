# SyndProxy validated proxy pool

## Current pool

- Alive now: 578
- Gold now: 424
- HTTP: 111 alive / 68 gold
- HTTPS: 113 alive / 24 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 183 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35546
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
