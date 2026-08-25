# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 411
- HTTP: 101 alive / 59 gold
- HTTPS: 68 alive / 19 gold
- SOCKS4: 183 alive / 162 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36219
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
