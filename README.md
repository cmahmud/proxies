# SyndProxy private pool

## Current pool

- Alive now: 1056
- Gold now: 407
- HTTP: 376 alive / 93 gold
- HTTPS: 238 alive / 32 gold
- SOCKS4: 212 alive / 140 gold
- SOCKS5: 230 alive / 142 gold

## Historical pool

- Discovered: 163252
- Ever alive: 31751
- Ever gold: 1166

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
