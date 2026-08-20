# SyndProxy private pool

## Current pool

- Alive now: 805
- Gold now: 384
- HTTP: 240 alive / 79 gold
- HTTPS: 128 alive / 15 gold
- SOCKS4: 226 alive / 152 gold
- SOCKS5: 211 alive / 138 gold

## Historical pool

- Discovered: 145552
- Ever alive: 25468
- Ever gold: 1060

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
