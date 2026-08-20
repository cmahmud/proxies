# SyndProxy private pool

## Current pool

- Alive now: 1636
- Gold now: 658
- HTTP: 654 alive / 216 gold
- HTTPS: 495 alive / 116 gold
- SOCKS4: 230 alive / 158 gold
- SOCKS5: 257 alive / 168 gold

## Historical pool

- Discovered: 141223
- Ever alive: 23933
- Ever gold: 964

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
