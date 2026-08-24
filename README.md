# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 389
- HTTP: 115 alive / 53 gold
- HTTPS: 55 alive / 13 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 200 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33382
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
