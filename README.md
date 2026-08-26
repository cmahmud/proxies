# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 397
- HTTP: 93 alive / 57 gold
- HTTPS: 82 alive / 14 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39157
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
