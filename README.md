# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 397
- HTTP: 140 alive / 72 gold
- HTTPS: 59 alive / 16 gold
- SOCKS4: 176 alive / 155 gold
- SOCKS5: 198 alive / 154 gold

## Historical pool

- Discovered: 176974
- Ever alive: 33264
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
