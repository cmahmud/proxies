# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 424
- HTTP: 306 alive / 87 gold
- HTTPS: 230 alive / 29 gold
- SOCKS4: 209 alive / 144 gold
- SOCKS5: 248 alive / 164 gold

## Historical pool

- Discovered: 161983
- Ever alive: 31239
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
