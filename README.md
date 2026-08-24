# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 389
- HTTP: 100 alive / 50 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33397
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
