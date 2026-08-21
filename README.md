# SyndProxy private pool

## Current pool

- Alive now: 1189
- Gold now: 426
- HTTP: 384 alive / 97 gold
- HTTPS: 307 alive / 27 gold
- SOCKS4: 220 alive / 147 gold
- SOCKS5: 278 alive / 155 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28227
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
