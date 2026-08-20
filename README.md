# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 354
- HTTP: 203 alive / 66 gold
- HTTPS: 138 alive / 18 gold
- SOCKS4: 232 alive / 144 gold
- SOCKS5: 210 alive / 126 gold

## Historical pool

- Discovered: 145548
- Ever alive: 25397
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
