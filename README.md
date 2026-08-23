# SyndProxy validated proxy pool

## Current pool

- Alive now: 713
- Gold now: 197
- HTTP: 288 alive / 36 gold
- HTTPS: 47 alive / 5 gold
- SOCKS4: 183 alive / 68 gold
- SOCKS5: 195 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32775
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
