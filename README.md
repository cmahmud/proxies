# SyndProxy private pool

## Current pool

- Alive now: 1046
- Gold now: 426
- HTTP: 315 alive / 86 gold
- HTTPS: 231 alive / 22 gold
- SOCKS4: 237 alive / 163 gold
- SOCKS5: 263 alive / 155 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30012
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
