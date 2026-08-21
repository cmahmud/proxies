# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 365
- HTTP: 415 alive / 92 gold
- HTTPS: 261 alive / 21 gold
- SOCKS4: 186 alive / 116 gold
- SOCKS5: 228 alive / 136 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28815
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
