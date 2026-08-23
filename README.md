# SyndProxy validated proxy pool

## Current pool

- Alive now: 709
- Gold now: 197
- HTTP: 270 alive / 36 gold
- HTTPS: 49 alive / 5 gold
- SOCKS4: 187 alive / 68 gold
- SOCKS5: 203 alive / 88 gold

## Historical pool

- Discovered: 170566
- Ever alive: 32775
- Ever gold: 1209

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
