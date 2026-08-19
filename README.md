# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 336
- HTTP: 323 alive / 66 gold
- HTTPS: 197 alive / 14 gold
- SOCKS4: 253 alive / 138 gold
- SOCKS5: 209 alive / 118 gold

## Historical pool

- Discovered: 109959
- Ever alive: 15358
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
