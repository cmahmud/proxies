# SyndProxy private pool

## Current pool

- Alive now: 1154
- Gold now: 423
- HTTP: 368 alive / 95 gold
- HTTPS: 296 alive / 27 gold
- SOCKS4: 231 alive / 147 gold
- SOCKS5: 259 alive / 154 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28236
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
