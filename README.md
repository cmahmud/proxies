# SyndProxy private pool

## Current pool

- Alive now: 1188
- Gold now: 566
- HTTP: 447 alive / 188 gold
- HTTPS: 272 alive / 111 gold
- SOCKS4: 244 alive / 123 gold
- SOCKS5: 225 alive / 144 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19284
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
