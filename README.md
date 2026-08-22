# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 353
- HTTP: 296 alive / 92 gold
- HTTPS: 148 alive / 26 gold
- SOCKS4: 186 alive / 112 gold
- SOCKS5: 216 alive / 123 gold

## Historical pool

- Discovered: 167410
- Ever alive: 32576
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
