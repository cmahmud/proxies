# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 397
- HTTP: 93 alive / 60 gold
- HTTPS: 174 alive / 13 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40647
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
