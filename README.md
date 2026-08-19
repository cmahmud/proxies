# SyndProxy private pool

## Current pool

- Alive now: 1139
- Gold now: 460
- HTTP: 402 alive / 119 gold
- HTTPS: 278 alive / 72 gold
- SOCKS4: 228 alive / 140 gold
- SOCKS5: 231 alive / 129 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16753
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
