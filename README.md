# SyndProxy private pool

## Current pool

- Alive now: 737
- Gold now: 380
- HTTP: 207 alive / 71 gold
- HTTPS: 103 alive / 22 gold
- SOCKS4: 224 alive / 144 gold
- SOCKS5: 203 alive / 143 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25424
- Ever gold: 1059

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
