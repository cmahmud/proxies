# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 407
- HTTP: 102 alive / 59 gold
- HTTPS: 157 alive / 15 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40775
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
