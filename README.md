# SyndProxy private pool

## Current pool

- Alive now: 924
- Gold now: 416
- HTTP: 258 alive / 93 gold
- HTTPS: 207 alive / 32 gold
- SOCKS4: 211 alive / 131 gold
- SOCKS5: 248 alive / 160 gold

## Historical pool

- Discovered: 162773
- Ever alive: 31669
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
