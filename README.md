# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 371
- HTTP: 332 alive / 86 gold
- HTTPS: 216 alive / 22 gold
- SOCKS4: 210 alive / 127 gold
- SOCKS5: 231 alive / 136 gold

## Historical pool

- Discovered: 158223
- Ever alive: 29825
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
