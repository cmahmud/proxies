# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 414
- HTTP: 109 alive / 69 gold
- HTTPS: 171 alive / 18 gold
- SOCKS4: 178 alive / 156 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40635
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
