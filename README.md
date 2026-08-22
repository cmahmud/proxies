# SyndProxy private pool

## Current pool

- Alive now: 1116
- Gold now: 426
- HTTP: 408 alive / 101 gold
- HTTPS: 278 alive / 32 gold
- SOCKS4: 190 alive / 135 gold
- SOCKS5: 240 alive / 158 gold

## Historical pool

- Discovered: 161019
- Ever alive: 31116
- Ever gold: 1154

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
