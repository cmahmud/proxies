# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 426
- HTTP: 320 alive / 97 gold
- HTTPS: 234 alive / 23 gold
- SOCKS4: 236 alive / 144 gold
- SOCKS5: 268 alive / 162 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28175
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
