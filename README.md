# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 404
- HTTP: 188 alive / 80 gold
- HTTPS: 144 alive / 26 gold
- SOCKS4: 228 alive / 154 gold
- SOCKS5: 223 alive / 144 gold

## Historical pool

- Discovered: 150213
- Ever alive: 27028
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
