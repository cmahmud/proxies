# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 397
- HTTP: 97 alive / 72 gold
- HTTPS: 45 alive / 17 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 169 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48188
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
